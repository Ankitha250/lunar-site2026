# Lunar Landing Site Navigator
### NASA Space Apps Challenge 2026 Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Verified-brightgreen.svg)]()
[![NASA Data](https://img.shields.io/badge/NASA%20Data-PGDA%20Product%2078%20%7C%20LOLA%20%7C%20Horizons-orange.svg)](https://pgda.gsfc.nasa.gov/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An end-to-end, decision-support platform and interactive 3D web application designed to evaluate, rank, and navigate optimal touchdown zones at the **Lunar South Pole** ($84^\circ\text{S} - 90^\circ\text{S}$) for NASA's Artemis III, Artemis IV, and CLPS missions.

---

## Project Structure

The repository is modularized into four clear directories:

```text
Lunar-Landing-Navigator/
├── frontend/                     # Interactive 3D Web Application
│   └── index.html                # Canvas 3D renderer, Dashboard, Regional Explorer, Solar & Comparison
├── backend/                      # Python REST API & Calculation Engine
│   ├── server.py                 # High-performance zero-dependency REST server & frontend host
│   ├── calculator.py             # Pure mathematical engine for all 8 core calculations
│   ├── test_backend.py           # Comprehensive unit tests for all calculations
│   └── requirements.txt          # Requirements specifications
├── data/                         # Verified Planetary Geodesy Datasets
│   ├── lunar_elevation_grid_5m.json / .csv      # 5m LOLA South Pole DEM matrix
│   ├── lunar_waypoints.json / .csv             # Candidate sites & science POI coordinates
│   ├── crater_hazards.json / .csv              # South Pole crater hazards & exclusion radii
│   ├── solar_illumination_ephemeris.json / .csv# Sun position & solar flux time-series
│   ├── calculation_parameters.json             # Mathematical formulas, thresholds & weights
│   └── CALCULATIONS_GUIDE.md                   # Detailed formulas documentation
├── docs/                         # Engineering & Mission Documentation
│   ├── ARCHITECTURE.md           # System architecture diagrams & data flow
│   ├── API_REFERENCE.md          # REST API endpoints reference & JSON schemas
│   └── SETUP_AND_RUN.md          # Deployment & execution instructions
├── start_navigator.bat           # 1-Click launcher for Windows
├── push_to_github.bat            # Automated Git push script
├── push_to_github.ps1            # Automated PowerShell Git push script
├── push_to_github_api.py         # Direct GitHub REST API uploader (no git CLI required)
├── .gitignore                    # Standard repository ignore file
└── README.md                     # Master project overview
```

---

## 8 Core Engineering Calculations

| # | Calculation | Method / Algorithm | Output |
|---|---|---|---|
| **1** | **Elevation Calculation** | Bilinear interpolation over LOLA 5m DEM | Terrain height $z$ relative to lunar datum |
| **2** | **Slope Calculation** | Horn's 3x3 convolution kernel | Gradient in degrees ($\le 5^\circ$ flat, $>10^\circ$ steep) |
| **3** | **Surface Roughness** | Terrain Roughness Index (TRI) | Micro-relief variance in meters |
| **4** | **Landing Safety Score** | Multi-Criteria Decision Analysis (MCDA) | Normalized Touchdown Suitability $[0.0 - 1.0]$ |
| **5** | **Distance Calculation** | Great-Circle Haversine & 3D Euclidean | True surface and spatial distances (km) |
| **6** | **Navigation Path Calculation**| A* (A-Star) Pathfinding | Safe traverse route avoiding $>15^\circ$ slopes |
| **7** | **Sunlight Illumination** | Horizon shadow ray-tracing | Binary shadow mask & solar power flux ($\text{W/m}^2$) |
| **8** | **Hazard Detection** | Slope thresholds + Crater safety buffers | Binary hazard mask ($1 = \text{Hazard}$, $0 = \text{Safe}$) |

---

## Quickstart: How to Run

### Method 1: 1-Click Launch (Windows)
Double-click:
```bash
start_navigator.bat
```
This boots the Python REST API server on `http://localhost:8000/` and opens the Navigator in your web browser.

### Method 2: Command Line
```bash
cd backend
python server.py
```
Open **`http://localhost:8000/`** in your browser.

### Run Tests:
```bash
cd backend
python test_backend.py
```

---

## Pushing to GitHub

To push this entire project to your team's GitHub repository:

### Option A: Using the Push Script (if Git is installed)
Run `push_to_github.bat` or `push_to_github.ps1`, enter your repository URL (e.g. `https://github.com/USERNAME/REPO.git`), and it will commit and push all files.

### Option B: Direct Python API Uploader (Zero Git Required)
If Git CLI is not installed on your computer, run:
```bash
python push_to_github_api.py
```
Enter your repo name (`owner/repo`) and your GitHub token to upload all files directly via GitHub's REST API!

---

## Official Data Citations
* **NASA Planetary Geodesy Data Archive:** [PGDA Product 78 (5 m/pixel LOLA Topography)](https://pgda.gsfc.nasa.gov/products/78)
* **USGS ScienceBase:** [Down-Selected Artemis III Candidate Navigational Grids (DOI: 10.5066/P13YPWQD)](https://doi.org/10.5066/P13YPWQD)
* **NASA JPL Horizons API:** [Solar System Dynamics Ephemeris System](https://ssd.jpl.nasa.gov/horizons/)
* **NASA LRO Diviner & LOLA Teams:** [Lunar Reconnaissance Orbiter Science Archive](https://pds-imaging.jpl.nasa.gov/portal/lro_mission.html)
