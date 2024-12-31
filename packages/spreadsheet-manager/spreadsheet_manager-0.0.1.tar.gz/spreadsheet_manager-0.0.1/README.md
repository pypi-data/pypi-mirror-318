# Spreadsheet Manager

**Spreadsheet Manager** is a lightweight Python package designed for loading and managing data from Google Sheets, fetching data from all tabs within the file. This package provides a simple interface for accessing and storing tabular data in JSON format.

---

## Features

- **Load All Tabs**: Fetch data from all tabs within a spreadsheet automatically.
- **Easy to Use**: Minimal setup to integrate into your projects.
- **Lightweight**: No unnecessary dependencies—uses only `pandas` and `json`.

---

## Installation

You can install **Spreadsheet Manager** via pip:

```bash
pip install spreadsheet-manager
```

---

## Usage

### Initializing the Manager

```python
from spreadsheet_manager import SheetsManager

# Initialize the SheetsManager with your Google Sheet ID
sheet_id = "your_google_sheet_id"
manager = SheetsManager(sheet_id)
```

### Loading All Tabs Data

```python
# Load data from all tabs
manager.load_all_tabs()

# Access the data as a dictionary
print(manager.sheet_data)  # Dictionary where keys are tab names and values are the tab data
```

---

## Getting the Sheet ID and Generating the URL

To use a Google Sheet with this package, you need the **Sheet ID**. Follow these steps:

### Step 1: Open the Google Sheet

1. Go to [Google Sheets](https://sheets.google.com/) and open your spreadsheet.

### Step 2: Retrieve the Sheet ID

1. Copy the URL from your browser’s address bar. It should look something like this:
   ```
   https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid=0
   ```
2. The part between `/d/` and `/edit` is your **Sheet ID**.

### Step 3: Publish the Google Sheet

1. Click on `File` in the top menu.
2. Select `Share` > `Publish to the web`.
3. In the dialog that opens, choose:
   - **Entire Document**: To make all tabs available.
   - **Microsoft Excel (.xlsx)** as the file format.
4. Click `Publish` and confirm your choice.

### Important Warning

- **Public Access**: Publishing makes the spreadsheet accessible to anyone with the link.
- **Read-Only**: Others can download the file but cannot directly edit it.

---

## Requirements

- Python 3.7+
- pandas

---

## Contributing

Contributions are welcome! If you encounter bugs, have feature requests, or want to contribute code, feel free to submit issues and pull requests on GitHub.

---

## License

**Spreadsheet Manager** is licensed under the MIT License. See the LICENSE file for more details.
