# IntergalacticCargoTriager-Lohith — Git Setup Guide
# ====================================================

# ─────────────────────────────────────────────────────
# RECOMMENDED FOLDER STRUCTURE (GitHub Repo Root)
# ─────────────────────────────────────────────────────
#
# IntergalacticCargoTriager-Lohith/
# ├── manifest.txt
# ├── parser.py
# ├── Task 1 - Lohith - Parser.json
# ├── README.md
# ├── backend/
# │   ├── app.py
# │   └── requirements.txt
# └── frontend/
#     ├── index.html
#     ├── package.json
#     ├── vite.config.js
#     └── src/
#         ├── main.jsx
#         ├── App.jsx
#         ├── index.css
#         └── components/
#             ├── CargoTable.jsx
#             ├── SyncButton.jsx
#             └── StatusBar.jsx

# ─────────────────────────────────────────────────────
# STEP 1: INITIALIZE REPOSITORY
# ─────────────────────────────────────────────────────

git init
git remote add origin https://github.com/Lohith2511/IntergalacticCargoTriager-Lohith.git

# ─────────────────────────────────────────────────────
# STEP 2: CREATE .gitignore
# ─────────────────────────────────────────────────────

# (Create .gitignore with the content in the .gitignore file)

# ─────────────────────────────────────────────────────
# COMMIT ORDER & MESSAGES
# ─────────────────────────────────────────────────────

# Commit 1 — Project scaffold
git add manifest.txt README.md
git commit -m "Initial project scaffold: added manifest.txt and folder structure"

# Commit 2 — Parser core logic
git add parser.py
git commit -m "feat(parser): implement manifest parser with Sector-7 multiplier"

# Commit 3 — Prime filter (contains "Anomaly" as required)
git add parser.py
git commit -m "feat(parser): add prime-number filter — Anomaly in CRG-002 and CRG-005 weight data discarded"

# Commit 4 — Parser output JSON
git add "Task 1 - Lohith - Parser.json"
git commit -m "feat(parser): generate Task 1 - Lohith - Parser.json output"

# Commit 5 — Flask API endpoint
git add backend/app.py
git commit -m "feat(backend): scaffold Flask API with GET /api/cargo endpoint"

# Commit 6 — System Override 418 guard
git add backend/app.py
git commit -m "feat(backend): add X-System-Override header guard (HTTP 418)"

# Commit 7 — CORS, error handlers, requirements
git add backend/requirements.txt backend/app.py
git commit -m "feat(backend): add CORS, error handlers, and requirements.txt"

# Commit 8 — React + Vite scaffold
git add frontend/
git commit -m "feat(frontend): scaffold React + Vite project"

# Commit 9 — CargoTable with sorting
git add frontend/src/components/CargoTable.jsx
git commit -m "feat(frontend): implement CargoTable with weight sort and Earth-last rule"

# Commit 10 — SyncButton
git add frontend/src/components/SyncButton.jsx frontend/src/components/StatusBar.jsx
git commit -m "feat(frontend): add SyncButton with 2.5-second animation cycle"

# Commit 11 — Premium UI design
git add frontend/src/index.css frontend/src/App.jsx frontend/src/main.jsx frontend/index.html
git commit -m "feat(frontend): apply premium dark space UI design system"

# Commit 12 — Docs
git add README.md
git commit -m "docs: add complete README"

# ─────────────────────────────────────────────────────
# STEP 3: PUSH TO GITHUB
# ─────────────────────────────────────────────────────

git branch -M main
git push -u origin main

# ─────────────────────────────────────────────────────
# VERIFY COMMIT LOG
# ─────────────────────────────────────────────────────

git log --oneline

# Expected output (newest first):
# abc1234 docs: add complete README
# def5678 feat(frontend): apply premium dark space UI design system
# ghi9012 feat(frontend): add SyncButton with 2.5-second animation cycle
# jkl3456 feat(frontend): implement CargoTable with weight sort and Earth-last rule
# mno7890 feat(frontend): scaffold React + Vite project
# pqr1234 feat(backend): add CORS, error handlers, and requirements.txt
# stu5678 feat(backend): add X-System-Override header guard (HTTP 418)
# vwx9012 feat(backend): scaffold Flask API with GET /api/cargo endpoint
# yza3456 feat(parser): generate Task 1 - Lohith - Parser.json output
# bcd7890 feat(parser): add prime-number filter — Anomaly in CRG-002 and CRG-005 weight data discarded
# efg1234 feat(parser): implement manifest parser with Sector-7 multiplier
# hij5678 Initial project scaffold: added manifest.txt and folder structure
