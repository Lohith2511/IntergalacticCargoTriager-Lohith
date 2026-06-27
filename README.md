# IntergalacticCargoTriager-Lohith

> **Real-time intergalactic cargo manifest intelligence — Python · Flask · React · Vite**

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Folder Structure](#folder-structure)  
3. [Installation](#installation)  
4. [Backend Setup](#backend-setup)  
5. [Frontend Setup](#frontend-setup)  
6. [Running Both Projects](#running-both-projects)  
7. [API Endpoint](#api-endpoint)  
8. [Git Commit History](#git-commit-history)  
9. [Screenshots](#screenshots)  

---

## Project Overview

| Task | Description |
|------|-------------|
| **Task 1 – Parser** | Reads `manifest.txt`, applies Sector-7 weight multiplier (×1.45), discards records whose rounded weight is prime, outputs `Task 1 - Lohith - Parser.json`. |
| **Task 2 – Backend API** | Flask REST API serving the parsed JSON. Blocks requests with `X-System-Override: true` header with HTTP 418. |
| **Task 3 – React Dashboard** | Vite + React dashboard that fetches live data, sorts by weight (Earth always last), and features an animated "Sync Data" button. |

---

## Folder Structure

```
IntergalacticCargo Triager/
│
├── manifest.txt                        # Raw cargo manifest input
├── parser.py                           # Task 1 — Parser script
├── Task 1 - Lohith - Parser.json       # Task 1 — Parser output (generated)
├── README.md                           # This file
│
├── backend/                            # Task 2 — Flask API
│   ├── app.py                          #   Flask application
│   └── requirements.txt                #   Python dependencies
│
└── frontend/                           # Task 3 — React + Vite Dashboard
    ├── index.html                       #   HTML shell (SEO meta tags)
    ├── package.json                     #   Node dependencies
    ├── vite.config.js                   #   Vite configuration + proxy
    └── src/
        ├── main.jsx                     #   React entry point
        ├── App.jsx                      #   Root component (fetch + layout)
        ├── index.css                    #   Global design system styles
        └── components/
            ├── CargoTable.jsx           #   Sortable cargo table
            ├── SyncButton.jsx           #   Sync button with 2.5s animation
            └── StatusBar.jsx            #   Loading / error feedback
```

---

## Installation

### Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.10+ |
| pip | latest |
| Node.js | 18+ |
| npm | 9+ |
| Git | 2.x |

### Clone / enter project

```bash
# If starting fresh from a git repo:
git clone <your-repo-url> IntergalacticCargoTriager-Lohith
cd "IntergalacticCargo Triager"
```

---

## Backend Setup

```bash
# Navigate to backend folder
cd backend

# Install Python dependencies
pip install -r requirements.txt
```

---

## Frontend Setup

```bash
# Navigate to frontend folder
cd frontend

# Install Node dependencies
npm install
```

---

## Running Both Projects

### Step 1 — Run the Parser (only needed once)

```bash
# From the project root
python parser.py
# Generates: Task 1 - Lohith - Parser.json
```

### Step 2 — Start the Flask backend

```bash
cd backend
python app.py
# Flask starts at: http://localhost:5000
```

### Step 3 — Start the React frontend

```bash
cd frontend
npm run dev
# Vite starts at: http://localhost:5173
```

Open your browser at **http://localhost:5173** to view the dashboard.

---

## API Endpoint

### `GET /api/cargo`

Returns the parsed cargo JSON array.

**Normal request:**
```bash
curl http://localhost:5000/api/cargo
```

**Response (200 OK):**
```json
[
  {
    "cargo_id": "CRG-001",
    "date": "2026-03-29",
    "destination": "Mars Base Alpha",
    "weight_in_kg": 500.0,
    "final_weight": 500,
    "sector7_applied": false
  },
  ...
]
```

---

### HTTP 418 — System Override

**Trigger command:**
```bash
curl -H "X-System-Override: true" http://localhost:5000/api/cargo
```

**Response (418 I'm a Teapot):**
```
System override denied.
```

---

### `GET /api/health`

Liveness probe.

```bash
curl http://localhost:5000/api/health
# {"status": "ok", "service": "IntergalacticCargoTriager API"}
```

---

## Git Commit History

> See **Git Commands** section for the exact commit order.

| # | Message |
|---|---------|
| 1 | `Initial project scaffold: added manifest.txt and folder structure` |
| 2 | `feat(parser): implement manifest parser with Sector-7 multiplier` |
| 3 | `feat(parser): add prime-number filter — Anomaly in CRG-002 and CRG-005 weight data discarded` |
| 4 | `feat(parser): generate Task 1 - Lohith - Parser.json output` |
| 5 | `feat(backend): scaffold Flask API with GET /api/cargo endpoint` |
| 6 | `feat(backend): add X-System-Override header guard (HTTP 418)` |
| 7 | `feat(backend): add CORS, error handlers, and requirements.txt` |
| 8 | `feat(frontend): scaffold React + Vite project` |
| 9 | `feat(frontend): implement CargoTable with weight sort and Earth-last rule` |
| 10 | `feat(frontend): add SyncButton with 2.5-second animation cycle` |
| 11 | `feat(frontend): apply premium dark space UI design system` |
| 12 | `docs: add complete README` |

---

## Screenshots

> **Replace these placeholders with actual screenshots after running the app.**

### Dashboard
![Dashboard Screenshot](./screenshots/dashboard.png)

### Cargo Table (sorted)
![Cargo Table Screenshot](./screenshots/cargo_table.png)

### Sync Button Animation
![Sync Animation Screenshot](./screenshots/sync_button.png)

### HTTP 418 Response
![418 Response](./screenshots/http_418.png)

---

*Built with ❤ by Lohith — IntergalacticCargoTriager-Lohith*
