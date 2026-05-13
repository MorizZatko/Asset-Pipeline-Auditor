# Asset Pipeline Auditor

## Overview
In large productions, asset metadata is often stored in "dirty" raw text files. 
Corrupted/Dirty data can cause critical failures in pipelines which leads to time consuming research and fixes. 

The *Asset Pipeline Auditor* is a tool designed to validate and clean asset-datasets with a report via standard output.
It transforms unstructured raw data into a Object-Oriented (OOP) hierarchy to perform a "Health Check" and generates a final Data-Frame report for the production leads.

## Key-Features
- **Robust Data Import:** Custom loader that handles corrupted lines and invalid data types without crashing, for 100% pipeline uptime.
- **OOP Architecture:**  Initializes a base "Asset" class with specialized subclasses for "MeshAssets" and "TextureAssets", allowing    specific validation by "Polygon" for mesh-assets and "Resolution" for texture-assets. 
- **Health Check:** Central manager "AssetLibrary" that audit every asset based on production budgets (Size & Versioning).
- **Data-Frame Report:** Converting all validated OOP-Data back into a Pandas Data-Frame for final analysis.

## Technical Stack
- **Language:** Python 3.13
- **Data Analysis:** Pandas, Numpy
- **Design Pattern:** Object-Oriented-Programming (OOP), Composition, Delegation and Modular-Architecture.

## System Structure
Tool follows a linear pipeline flow:
*Raw Text File -> Pandas DataFrame -> OOP Asset Objects -> Health Audit -> Final Report (DataFrame)*

## Folder Structure:
- **src/models.py:** Contains the class hierarchy ("Asset", "MeshAsset", "TextureAsset", "AssetLibrary").
- **src/loader.py:** Handles safe reading and initial validation of the raw data.
- **main.py:** The entry point that manages the entire pipeline tool.
- **data/:** Contains the raw input file for the auditor as an example.

## How to Run
**1. Clone the repository:**
*Bash:*
git clone https://github.com/YourUsername/Asset-Pipeline-Auditor.git
**2. Install Dependencies when needed:**
*Bash:*
pip install pandas numpy
**3. Run the Tool:**
*Bash:*
python main.py

## Results
| Name | Category | Version | Size (MB) | Status |
| :--- | :--- | :--- | :--- | :--- |
| Hero_Mesh | Mesh | 1.2 | 500.0 | Outdated |
| Skin_Tex | Texture | 2.0 | 40.0 | OK |
| Rock_Mesh | Mesh | 1.1 | 1200.0 | Too heavy |