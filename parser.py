"""
IntergalacticCargoTriager - Task 1: Parser
==========================================
Author  : Lohith
Purpose : Parse manifest.txt, apply business rules, and output a clean JSON file.

Business Rules:
  1. Read manifest.txt and parse each record.
  2. If DESTINATION contains the exact substring "Sector-7", multiply WEIGHT_IN_KG by 1.45.
  3. Round the final weight to the nearest whole number.
  4. If the rounded weight is a prime number, discard the record completely.
  5. Save the remaining records into: "Task 1 - Lohith - Parser.json"
"""

import re
import json
import math
import os


# ---------------------------------------------------------------------------
# Prime-number utility
# ---------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """
    Return True if *n* is a prime number, False otherwise.

    Uses trial-division up to sqrt(n) for O(√n) time complexity.
    Edge cases handled: n ≤ 1 is not prime, 2 is prime, even numbers > 2 are not prime.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Only check odd divisors up to √n
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


# ---------------------------------------------------------------------------
# Manifest parser
# ---------------------------------------------------------------------------

# Pattern: [DATE] || CARGO_ID :: WEIGHT >> DESTINATION
# Example: [2026-03-29] || CRG-001 :: 500 >> Mars Base Alpha
MANIFEST_PATTERN = re.compile(
    r"\[(?P<date>[^\]]+)\]\s*\|\|\s*(?P<cargo_id>\S+)\s*::\s*(?P<weight>[\d.]+)\s*>>\s*(?P<destination>.+)"
)

SECTOR_7_SUBSTRING = "Sector-7"
SECTOR_7_MULTIPLIER = 1.45


def parse_manifest(filepath: str) -> list[dict]:
    """
    Read *filepath* line by line and parse every non-empty line into a
    raw cargo record dictionary.

    Returns a list of raw record dicts with keys:
      date, cargo_id, weight_in_kg (float), destination
    """
    records = []

    with open(filepath, "r", encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                # Skip blank lines
                continue

            match = MANIFEST_PATTERN.match(line)
            if not match:
                print(f"  [WARNING] Line {line_number} does not match expected format: {line!r}")
                continue

            raw_weight = float(match.group("weight"))
            records.append(
                {
                    "date": match.group("date"),
                    "cargo_id": match.group("cargo_id"),
                    "weight_in_kg": raw_weight,
                    "destination": match.group("destination").strip(),
                }
            )

    print(f"  Parsed {len(records)} raw records from '{filepath}'.")
    return records


# ---------------------------------------------------------------------------
# Business-rule processing
# ---------------------------------------------------------------------------

def apply_sector7_multiplier(record: dict) -> dict:
    """
    If the record's destination contains the exact substring 'Sector-7',
    multiply weight_in_kg by SECTOR_7_MULTIPLIER (1.45).

    Returns a *new* dict with an updated 'weight_in_kg' and an extra flag
    'sector7_multiplied' for auditability.
    """
    result = dict(record)
    if SECTOR_7_SUBSTRING in result["destination"]:
        original = result["weight_in_kg"]
        result["weight_in_kg"] = original * SECTOR_7_MULTIPLIER
        result["sector7_multiplied"] = True
        print(
            f"  [Sector-7] {result['cargo_id']} — weight {original} × {SECTOR_7_MULTIPLIER} = {result['weight_in_kg']}"
        )
    else:
        result["sector7_multiplied"] = False
    return result


def apply_rounding(record: dict) -> dict:
    """
    Round weight_in_kg to the nearest whole number and store it as
    'final_weight' (int). The original float is preserved.
    """
    result = dict(record)
    result["final_weight"] = round(result["weight_in_kg"])
    return result


def process_records(raw_records: list[dict]) -> list[dict]:
    """
    Apply the full business-rule pipeline to every raw record and return
    only those records whose final_weight is NOT a prime number.

    Pipeline per record:
      1. Apply Sector-7 multiplier (if applicable).
      2. Round to nearest whole number.
      3. Discard if rounded weight is prime.
    """
    kept = []
    discarded = []

    for record in raw_records:
        # Step 1 – Sector-7 weight adjustment
        record = apply_sector7_multiplier(record)

        # Step 2 – Round to nearest whole number
        record = apply_rounding(record)

        # Step 3 – Prime-number filter
        if is_prime(record["final_weight"]):
            discarded.append(record["cargo_id"])
            print(
                f"  [DISCARDED] {record['cargo_id']} — final weight {record['final_weight']} is prime."
            )
        else:
            kept.append(record)

    print(f"\n  Kept     : {len(kept)} records")
    print(f"  Discarded: {len(discarded)} records -> {discarded}")
    return kept


# ---------------------------------------------------------------------------
# Output builder
# ---------------------------------------------------------------------------

def build_output_records(processed: list[dict]) -> list[dict]:
    """
    Convert internal records to the clean JSON output format.

    Output schema per record:
      cargo_id        – string
      date            – string (original manifest date)
      destination     – string
      weight_in_kg    – float  (original weight before any multiplier)
      final_weight    – int    (after multiplier + rounding)
      sector7_applied – bool   (True if Sector-7 multiplier was used)
    """
    output = []
    for r in processed:
        output.append(
            {
                "cargo_id": r["cargo_id"],
                "date": r["date"],
                "destination": r["destination"],
                "weight_in_kg": r["weight_in_kg"],
                "final_weight": r["final_weight"],
                "sector7_applied": r["sector7_multiplied"],
            }
        )
    return output


def save_json(data: list[dict], output_path: str) -> None:
    """Serialise *data* to a pretty-printed JSON file at *output_path*."""
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=4, ensure_ascii=False)
    print(f"\n  Output saved -> {output_path}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  IntergalacticCargoTriager — Task 1: Parser")
    print("=" * 60)

    # Resolve paths relative to this script's location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(base_dir, "manifest.txt")
    output_path = os.path.join(base_dir, "Task 1 - Lohith - Parser.json")

    # --- Parse ---
    print("\n[1/4] Parsing manifest...")
    raw_records = parse_manifest(manifest_path)

    # --- Process ---
    print("\n[2/4] Applying business rules...")
    processed = process_records(raw_records)

    # --- Build clean output ---
    print("\n[3/4] Building output records...")
    output_records = build_output_records(processed)

    # --- Save ---
    print("\n[4/4] Saving JSON output...")
    save_json(output_records, output_path)

    print("\n" + "=" * 60)
    print(f"  Done! {len(output_records)} cargo records written.")
    print("=" * 60)


if __name__ == "__main__":
    main()
