# Apple Card Statement PDF to Excel

A Python script that automatically extracts transactions from Apple Card PDF statements and exports them into a structured Excel file. Demonstrates PDF text extraction, pattern recognition with regular expressions, data cleaning, and Excel automation using Python.

---

## Project Overview

This script reads an Apple Card PDF statement, detects transactions based on the date format (MM/DD/YYYY), and extracts the **Date**, **Merchant information**, and **Amounts**. The transactions are then exported to an Excel file for easy viewing and further analysis.

The goal is to save time and avoid manually copying transaction data from PDFs to spreadsheets.

---

## Features

- Reads and processes Apple Card PDF statements page by page  
- Identifies transaction lines using a date pattern (MM/DD/YYYY)  
- Extracts and cleans transaction data: "Merchant Name", "Date", "Amount", "Merchant Information", "Daily Cash %", "Daily Cash"  
- Removes `$` symbols and commas from amounts  
- Exports the clean data to an Excel file (`.xlsx`)  

---

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd pdfReader
```
2. Create and activate a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .\.venv\Scripts\activate  # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
---

## Usage

1.	Place your Apple Card PDF statement in the project folder.
2.	Edit the pdfPath variable in readFile.py to point to your PDF:
   ```pdfPath = "Apple Card Statement - MONTH YEAR.pdf"```
3. Run the script
   ```python3 (or python) readFile.py```
4. Script generates Excel file with trascations, check project folder for output file

---
## Notes
-	The script currently expects Apple Card statements, but it can be adapted for other credit card PDFs with similar formatting.
-	Make sure to replace placeholder filenames with your actual statement PDF.
- .DS_Store and .venv should be ignored via .gitignore to keep the repository clean.

---
