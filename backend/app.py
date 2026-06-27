"""
IntergalacticCargoTriager - Task 2: Flask REST API
===================================================
Author  : Lohith
Purpose : Serve the parsed cargo JSON via a REST endpoint with
          special handling for the X-System-Override header.

Endpoints:
  GET /api/cargo
    - Returns the cargo JSON array.
    - If the request header "X-System-Override: true" is present,
      responds with HTTP 418 and body "System override denied."

Usage:
  pip install -r requirements.txt
  python app.py
  # Server starts on http://localhost:5000
"""

import json
import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

# ---------------------------------------------------------------------------
# App initialisation
# ---------------------------------------------------------------------------

app = Flask(__name__)

# Enable CORS so the React frontend (running on a different port) can fetch data.
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

# The parser output JSON lives one directory above this file (project root).
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARGO_JSON_PATH = os.path.join(BASE_DIR, "..", "Task 1 - Lohith - Parser.json")


def load_cargo_data() -> list[dict]:
    """
    Load and return the cargo records from the Task-1 output JSON file.

    Raises:
        FileNotFoundError: if the JSON file is missing.
        ValueError:        if the JSON cannot be decoded.
    """
    resolved = os.path.normpath(CARGO_JSON_PATH)
    if not os.path.isfile(resolved):
        raise FileNotFoundError(f"Cargo data file not found: {resolved}")

    with open(resolved, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    if not isinstance(data, list):
        raise ValueError("Cargo JSON must be a top-level array.")

    return data


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/api/cargo", methods=["GET"])
def get_cargo():
    """
    GET /api/cargo

    Returns the parsed cargo JSON array.

    Special behaviour:
      If the request header X-System-Override is exactly 'true',
      respond with HTTP 418 I'm a Teapot and the message
      "System override denied."
    """
    # --- System-Override guard ---
    override_header = request.headers.get("X-System-Override", "")
    if override_header.lower() == "true":
        app.logger.warning("System override attempt detected — request blocked.")
        return Response(
            response="System override denied.",
            status=418,
            mimetype="text/plain",
        )

    # --- Normal flow ---
    try:
        cargo_data = load_cargo_data()
        return jsonify(cargo_data), 200

    except FileNotFoundError as exc:
        app.logger.error("Cargo data file missing: %s", exc)
        return jsonify({"error": "Cargo data not found. Run the parser first."}), 404

    except (ValueError, json.JSONDecodeError) as exc:
        app.logger.error("Failed to decode cargo data: %s", exc)
        return jsonify({"error": "Cargo data is corrupted or invalid."}), 500

    except Exception as exc:  # pylint: disable=broad-except
        app.logger.error("Unexpected error: %s", exc)
        return jsonify({"error": "An unexpected server error occurred."}), 500


# ---------------------------------------------------------------------------
# Health-check route (bonus convenience endpoint)
# ---------------------------------------------------------------------------

@app.route("/api/health", methods=["GET"])
def health_check():
    """GET /api/health — Simple liveness probe."""
    return jsonify({"status": "ok", "service": "IntergalacticCargoTriager API"}), 200


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def not_found(error):
    """Return a JSON 404 response for unknown routes."""
    return jsonify({"error": "Endpoint not found.", "detail": str(error)}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Return a JSON 405 response for disallowed methods."""
    return jsonify({"error": "Method not allowed.", "detail": str(error)}), 405


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Run with debug=False in a production deployment.
    # For local development, debug=True provides auto-reload and better tracebacks.
    app.run(host="0.0.0.0", port=5000, debug=True)
