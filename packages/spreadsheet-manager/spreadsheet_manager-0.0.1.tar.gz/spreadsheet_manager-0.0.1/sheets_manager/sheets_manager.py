import pandas as pd
import json

class SheetsManager:
    """
    A class to manage and load Google Sheets data from all tabs.
    
    Attributes:
        sheet_id (str): The ID of the Google Sheet.
        sheet_data (dict): A dictionary to store the data loaded from all tabs.
    """

    def __init__(self, sheet_id):
        """
        Initialize the SheetsManager with a Google Sheet URL.

        Args:
            sheet_url (str): The URL of the Google Sheet.
        """
        self.sheet_url = f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?output=xlsx"
        self.sheet_data = {}

    def load_all_tabs(self):
        """
        Load data from all tabs in the Google Sheet.

        Raises:
            ValueError: If there is an issue loading the data.
        """
        try:
            xls = pd.ExcelFile(self.sheet_url)
            for sheet_name in xls.sheet_names:
                rows_data = pd.read_excel(xls, sheet_name)
                rows_data = json.loads(rows_data.to_json(orient='records'))
                self.sheet_data[sheet_name] = rows_data
        except Exception as e:
            raise ValueError(f"Error loading data from spreadsheet: {e}")

