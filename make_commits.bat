@echo off
REM Git commit script for IntergalacticCargoTriager-Lohith
REM Run this from the project root

REM Commit 4: Parser output JSON
git add "Task 1 - Lohith - Parser.json"
git commit -m "feat(parser): generate Task 1 - Lohith - Parser.json output"

REM Commit 5: Flask API scaffold
git add backend/app.py
git commit -m "feat(backend): scaffold Flask API with GET /api/cargo endpoint"

REM Commit 6: System Override 418
git add backend/app.py
git commit -m "feat(backend): add X-System-Override header guard HTTP 418"

REM Commit 7: CORS, error handlers, requirements
git add backend/requirements.txt backend/test_api.py
git commit -m "feat(backend): add CORS error handlers and requirements.txt"

REM Commit 8: React + Vite scaffold
git add frontend/package.json frontend/vite.config.js frontend/index.html
git commit -m "feat(frontend): scaffold React + Vite project"

REM Commit 9: CargoTable with sorting
git add frontend/src/components/CargoTable.jsx
git commit -m "feat(frontend): implement CargoTable with weight sort and Earth-last rule"

REM Commit 10: SyncButton + StatusBar
git add frontend/src/components/SyncButton.jsx frontend/src/components/StatusBar.jsx
git commit -m "feat(frontend): add SyncButton with 2.5-second animation cycle"

REM Commit 11: Premium UI
git add frontend/src/index.css frontend/src/App.jsx frontend/src/main.jsx
git commit -m "feat(frontend): apply premium dark space UI design system"

REM Commit 12: Docs and submission
git add README.md GIT_COMMANDS.sh submission_emails.py
git commit -m "docs: add complete README Git commands and submission emails"

echo.
echo === All commits done! ===
git log --oneline
