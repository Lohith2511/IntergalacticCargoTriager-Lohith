"""
SUBMISSION EMAILS — IntergalacticCargoTriager-Lohith
=====================================================
Copy the relevant email below and send to your instructor.
"""

# ==========================================================================
# EMAIL 1 — Task 1 Submission (Parser)
# ==========================================================================

TASK_1_EMAIL = """
Subject: Task 1 Submission – IntergalacticCargoTriager Parser – Lohith

Dear [Instructor Name],

Please find my submission for Task 1 of the IntergalacticCargoTriager assignment.

── What I Built ──────────────────────────────────────────────────────────────

Task 1 required building a Python parser to process the intergalactic cargo
manifest and apply a series of business rules.

Implementation Summary:
• Script      : parser.py
• Input       : manifest.txt  (12 raw cargo records)
• Output      : Task 1 - Lohith - Parser.json  (10 valid records)

Business Rules Applied:
1. Parsed all 12 records from manifest.txt using regex.
2. Applied the Sector-7 weight multiplier (×1.45) to destinations containing
   the exact substring "Sector-7":
     - CRG-005 : 20 kg × 1.45 = 29 kg
     - CRG-012 : 100 kg × 1.45 = 145 kg
3. Rounded all final weights to the nearest whole number.
4. Discarded records where the rounded weight is a prime number:
     - CRG-002 : weight 17 (prime) → DISCARDED
     - CRG-005 : weight 29 (prime) → DISCARDED
5. Saved the remaining 10 records to: Task 1 - Lohith - Parser.json

Code Quality:
• PEP8 compliant
• Fully modular (parse_manifest, apply_sector7_multiplier, apply_rounding,
  is_prime, process_records, build_output_records, save_json)
• Thoroughly commented
• Proper prime-number function using trial division up to √n

Git Commits for Task 1:
1. "Initial project scaffold: added manifest.txt and folder structure"
2. "feat(parser): implement manifest parser with Sector-7 multiplier"
3. "feat(parser): add prime-number filter — Anomaly in CRG-002 and CRG-005 weight data discarded"
4. "feat(parser): generate Task 1 - Lohith - Parser.json output"

GitHub Repository: https://github.com/<your-username>/IntergalacticCargoTriager-Lohith

Please let me know if you have any questions.

Best regards,
Lohith
"""


# ==========================================================================
# EMAIL 2 — Task 2 Submission (Backend API)
# ==========================================================================

TASK_2_EMAIL = """
Subject: Task 2 Submission – IntergalacticCargoTriager Flask API – Lohith

Dear [Instructor Name],

Please find my submission for Task 2 of the IntergalacticCargoTriager assignment.

── What I Built ──────────────────────────────────────────────────────────────

Task 2 required building a Flask REST API to serve the parsed cargo data.

Implementation Summary:
• File         : backend/app.py
• Dependencies : backend/requirements.txt  (Flask==3.1.0, flask-cors==5.0.1)
• Endpoint     : GET /api/cargo

Running the Server:
────────────────────
  cd backend
  pip install -r requirements.txt
  python app.py
  # Server starts at: http://localhost:5000

Normal API Request:
───────────────────
  curl http://localhost:5000/api/cargo
  → Returns: HTTP 200 with JSON array of 10 cargo records.

HTTP 418 — System Override (exact curl command):
────────────────────────────────────────────────
  curl -H "X-System-Override: true" http://localhost:5000/api/cargo
  → Returns: HTTP 418 I'm a Teapot
             Body: System override denied.

Additional Features:
• CORS enabled via flask-cors (allows frontend at localhost:5173)
• GET /api/health — liveness probe
• JSON error handlers for 404 and 405 responses
• Proper logging of override attempts

Git Commits for Task 2:
5. "feat(backend): scaffold Flask API with GET /api/cargo endpoint"
6. "feat(backend): add X-System-Override header guard (HTTP 418)"
7. "feat(backend): add CORS, error handlers, and requirements.txt"

GitHub Repository: https://github.com/<your-username>/IntergalacticCargoTriager-Lohith

Please let me know if you have any questions.

Best regards,
Lohith
"""


# ==========================================================================
# EMAIL 3 — Final Submission (All Tasks)
# ==========================================================================

FINAL_SUBMISSION_EMAIL = """
Subject: Final Submission – IntergalacticCargoTriager-Lohith – All Tasks Complete

Dear [Instructor Name],

I am pleased to submit my completed IntergalacticCargoTriager assignment.
All three tasks have been implemented as per the specification.

── Project Details ────────────────────────────────────────────────────────────

Project Name  : IntergalacticCargoTriager-Lohith
GitHub        : https://github.com/<your-username>/IntergalacticCargoTriager-Lohith
Tech Stack    : Python, Flask, React + Vite, Git, JSON

── Task Summary ──────────────────────────────────────────────────────────────

TASK 1 — Python Parser (parser.py)
• Reads manifest.txt (12 records)
• Applies Sector-7 weight multiplier (×1.45) where destination contains "Sector-7"
• Rounds final weight to nearest whole number
• Discards records with prime-number weight (CRG-002: 17, CRG-005: 29)
• Outputs 10 valid records to: Task 1 - Lohith - Parser.json
• Modular, PEP8-compliant code with proper prime-number function

TASK 2 — Flask REST API (backend/app.py)
• GET /api/cargo — returns parsed JSON (HTTP 200)
• X-System-Override: true header → HTTP 418 "System override denied."
• CORS enabled for React frontend
• requirements.txt included
• Exact curl command to trigger HTTP 418:
    curl -H "X-System-Override: true" http://localhost:5000/api/cargo

TASK 3 — React + Vite Dashboard (frontend/)
• Fetches data from Flask backend
• Displays responsive table with:
    - Sorted by final_weight descending
    - Earth destinations always pinned to the bottom
• "Sync Data" button with exact 2.5-second animation:
    1. Button disabled
    2. Text changes to "Aligning quantum drives..."
    3. Waits exactly 2500ms
    4. Text restores to "Sync Data"
    5. Button re-enabled
• Premium dark-space UI with glassmorphism, animated starfield,
  weight bar indicators, destination icons, and micro-animations
• Modular components: App.jsx, CargoTable.jsx, SyncButton.jsx, StatusBar.jsx

── How to Run ────────────────────────────────────────────────────────────────

# Step 1: Run parser
python parser.py

# Step 2: Start backend
cd backend && python app.py

# Step 3: Start frontend (new terminal)
cd frontend && npm run dev

# Open browser at: http://localhost:5173

── Git Commits (12 total, 1 contains "Anomaly") ─────────────────────────────

1.  Initial project scaffold: added manifest.txt and folder structure
2.  feat(parser): implement manifest parser with Sector-7 multiplier
3.  feat(parser): add prime-number filter — Anomaly in CRG-002 and CRG-005 weight data discarded   ← contains "Anomaly"
4.  feat(parser): generate Task 1 - Lohith - Parser.json output
5.  feat(backend): scaffold Flask API with GET /api/cargo endpoint
6.  feat(backend): add X-System-Override header guard (HTTP 418)
7.  feat(backend): add CORS, error handlers, and requirements.txt
8.  feat(frontend): scaffold React + Vite project
9.  feat(frontend): implement CargoTable with weight sort and Earth-last rule
10. feat(frontend): add SyncButton with 2.5-second animation cycle
11. feat(frontend): apply premium dark space UI design system
12. docs: add complete README

Please feel free to reach out if you need any clarification.

Best regards,
Lohith
"""

if __name__ == "__main__":
    print("=" * 70)
    print("TASK 1 EMAIL")
    print("=" * 70)
    print(TASK_1_EMAIL)

    print("=" * 70)
    print("TASK 2 EMAIL")
    print("=" * 70)
    print(TASK_2_EMAIL)

    print("=" * 70)
    print("FINAL SUBMISSION EMAIL")
    print("=" * 70)
    print(FINAL_SUBMISSION_EMAIL)
