# 🌌 Intergalactic Cargo Triager

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.1.0-green?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![React Version](https://img.shields.io/badge/react-18%2B-cyan?logo=react&logoColor=white)](https://react.dev/)
[![Vite Version](https://img.shields.io/badge/vite-8.1.0-purple?logo=vite&logoColor=white)](https://vite.dev/)

> **Real-time intergalactic cargo manifest intelligence system.** Fully modular pipeline parsing quantum cargo manifests, applying celestial adjustments, exposing a secure Flask REST API, and rendering a premium dark-mode space telemetry dashboard.

---

## 📋 Table of Contents
* [🚀 Project Overview](#-project-overview)
* [📁 Directory Structure](#-directory-structure)
* [⚙️ Core Workflows & Rules](#-core-workflows--rules)
  * [Task 1: Manifest Parser](#task-1-manifest-parser)
  * [Task 2: Flask REST API](#task-2-flask-rest-api)
  * [Task 3: React Web Dashboard](#task-3-react-web-dashboard)
* [💻 Installation & Setup](#-installation--setup)
* [📡 API Telemetry Specs](#-api-telemetry-specs)
* [🐙 Git Control History](#-git-control-history)
* [📸 Interface Telemetry (Screenshots)](#-interface-telemetry-screenshots)

---

## 🚀 Project Overview

This full-stack system is divided into three key services:
1. **The Core Parser (`parser.py`):** Automatically consumes physical shipping manifests, scales masses according to coordinates, performs prime-number anomaly filtration, and generates sanitized JSON outputs.
2. **The REST Gateway (`backend/`):** A robust Flask microservice designed to serve clean JSON data with dynamic CORS support, endpoint protection (System Override Denial), and clean HTTP state responses.
3. **The Telemetry Dashboard (`frontend/`):** A high-fidelity, single-page application built on Vite + React featuring interactive animations, custom weight representation bars, and advanced gravity sorting (Earth-pinning logic).

---

## 📁 Directory Structure

```directory
IntergalacticCargoTriager-Lohith/
│
├── manifest.txt                        # Input cargo manifest
├── parser.py                           # Task 1: Parser script
├── Task 1 - Lohith - Parser.json       # Task 1: Cleaned JSON dataset
├── README.md                           # Documentation
├── GIT_COMMANDS.sh                     # Step-by-step git script
├── submission_emails.py                # Pre-formatted delivery emails
│
├── backend/                            # Task 2: REST API
│   ├── app.py                          # Flask entrypoint
│   ├── requirements.txt                # Python backend dependencies
│   └── test_api.py                     # Integration test suite
│
└── frontend/                           # Task 3: React SPA Dashboard
    ├── index.html                      # HTML shell & SEO meta-tags
    ├── package.json                    # Node dependencies
    ├── vite.config.js                  # Vite configuration & dev API proxy
    └── src/
        ├── main.jsx                    # React entrypoint
        ├── App.jsx                     # Core application controller
        ├── index.css                   # Premium global styling system
        └── components/
            ├── CargoTable.jsx          # Sortable telemetry view
            ├── SyncButton.jsx          # Quantum drives alignment button
            └── StatusBar.jsx           # Link state communicator
```

---

## ⚙️ Core Workflows & Rules

### Task 1: Manifest Parser

The Python program reads raw manifest rows matching:
`[DATE] || CARGO_ID :: WEIGHT >> DESTINATION`

#### 🛸 Business Rules Applied:
* **Sector-7 Gravity Well:** If the destination contains the substring `"Sector-7"`, the parser multiplies its `WEIGHT_IN_KG` by `1.45` to correct for gravitational drift.
* **Whole Number Rounding:** The final weight is rounded to the nearest integer.
* **Anomaly Deletion:** If the resulting rounded weight is a **Prime Number**, the cargo record contains quantum impurities and is **completely discarded**.

> [!NOTE]
> During parser execution:
> * `CRG-002` (Lunar Outpost Delta, weight 17) is discarded because `17` is prime.
> * `CRG-005` (Sector-7 Mining Rig, weight 20) becomes `20 * 1.45 = 29`. Since `29` is prime, it is also discarded.

---

### Task 2: Flask REST API

Exposes a backend service supporting standard cross-origin resource requests (CORS).

#### 🛡️ Quantum Override Protection:
If a client issues a request containing the HTTP header:
`X-System-Override: true`

The API instantly flags it as an unauthorized intervention, terminates the response, and returns:
* **HTTP Status Code:** `418 I'm a Teapot`
* **Response Body:** `System override denied.`
  <img width="550" height="227" alt="Task 2 - Screenshot 1 - Lohith - 418 I&#39;m a teapot png" src="https://github.com/user-attachments/assets/2638183c-53de-4f76-891d-f0d09ad2cec6" />


---

### Task 3: React Web Dashboard

A premium, responsive UI featuring an animated starfield background, glassmorphism overlays, and visual weight bars.

#### 🗂️ Sorting Exception:
All cargo records are sorted by their final weight in descending order (**highest to lowest**). However, any cargo shipping to **Earth** must automatically sink to the **absolute bottom of the table**, regardless of its weight.

#### ⚡ Quantum Sync Button:
When the "Sync Data" button is activated:
1. The button changes its state to `disabled`.
2. The button label changes to `Aligning quantum drives...`.
3. The application waits exactly `2.5 seconds` (simulating active engine calibration).
4. The button restores its label to `Sync Data` and is re-enabled.

---

## 💻 Installation & Setup

### Prerequisites
* **Python** 3.10 or higher
* **Node.js** 18 or higher (with npm)

### Setup & Run Steps

#### 1. Compile the Data
Run the parser program in the project root folder:
```bash
python parser.py
```
This parses `manifest.txt` and creates `Task 1 - Lohith - Parser.json`.

#### 2. Start the Backend API Server
```bash
cd backend
pip install -r requirements.txt
python app.py
```
*The Flask server is now listening at [http://localhost:5000](http://localhost:5000)*.

#### 3. Start the Web UI Development Server
```bash
cd ../frontend
npm install
npm run dev
```
*Open [http://localhost:5173](http://localhost:5173) in your web browser*.

---

## 📡 API Telemetry Specs

### Get Cargo Records
* **Endpoint:** `GET /api/cargo`
* **Normal Command:**
  ```bash
  curl http://localhost:5000/api/cargo
  ```
* **Payload Example (200 OK):**
  ```json
  [
    {
      "cargo_id": "CRG-001",
      "date": "2026-03-29",
      "destination": "Mars Base Alpha",
      "weight_in_kg": 500.0,
      "final_weight": 500,
      "sector7_applied": false
    }
  ]
  ```

### System Override Guard Response
* **Endpoint:** `GET /api/cargo`
* **Header Override Command:**
  ```bash
  curl -H "X-System-Override: true" http://localhost:5000/api/cargo
  ```
* **Response Output (418 I'm a Teapot):**
  ```text
  System override denied.
  ```

---

## 🐙 Git Control History

Below is the verified timeline of Git commits executed on this repository:

| Step | Commit Message |
|:---:|---|
| **1** | `Initial project scaffold: added manifest.txt and folder structure` |
| **2** | `feat(parser): implement manifest parser with Sector-7 multiplier` |
| **3** | `feat(parser): add prime-number filter -- Anomaly in CRG-002 and CRG-005 weight data discarded` |
| **4** | `feat(parser): generate Task 1 - Lohith - Parser.json output` |
| **5** | `feat(backend): scaffold Flask API with GET /api/cargo endpoint` |
| **6** | `feat(backend): add X-System-Override header guard HTTP 418` |
| **7** | `feat(backend): add CORS error handlers and requirements.txt` |
| **8** | `feat(frontend): scaffold React + Vite project` |
| **9** | `feat(frontend): implement CargoTable with weight sort and Earth-last rule` |
| **10** | `feat(frontend): add SyncButton with 2.5-second animation cycle` |
| **11** | `feat(frontend): apply premium dark space UI design system` |
| **12** | `docs: add complete README Git commands and submission emails` |

---

## 📸 Interface Telemetry (Screenshots)

> [!TIP]
> After launching both project applications locally, capture screenshots of the browser viewport and store them in a `./screenshots` subdirectory.

#### Main Telemetry Control Dashboard
![Dashboard View](./screenshots/dashboard.png)

#### Sorted Manifest View (Earth Pinned to Bottom)
![Sorted Table View](./screenshots/cargo_table.png)

#### Sync Button State Transitions
![Sync Transition View](./screenshots/sync_button.png)

#### API Block Response (Override Intercepted)
![System Override View](./screenshots/http_418.png)

---

*Custom engineered by Lohith. Intergalactic Cargo Triager 2026.*
