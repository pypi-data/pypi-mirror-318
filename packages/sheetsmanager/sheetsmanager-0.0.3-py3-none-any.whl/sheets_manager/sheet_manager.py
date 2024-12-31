import pandas as pd
import json

class SheetManager:
    # Class-level variables to store the URL and sheet data
    sheet_url = ""
    sheet_data = {}

    """
    A class to manage and load Google Sheets data from all tabs.

    Attributes:
        sheet_url (str): The URL of the Google Sheet.
        sheet_data (dict): A dictionary to store the data loaded from all tabs.
    """

    @staticmethod
    def init(sheet_id):
        """
        Initialize the SheetsManager with a Google Sheet ID.

        This method constructs the Google Sheets URL for the given sheet_id
        and initializes an empty dictionary to store the sheet data.

        Args:
            sheet_id (str): The ID of the Google Sheet to load data from.
        """
        SheetManager.sheet_url = f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?output=xlsx"
        SheetManager.sheet_data = SheetManager.reload()

    @staticmethod
    def reload():
        """
        Load data from all tabs in the Google Sheet.

        This method fetches the data from the Google Sheets URL and loads all tabs into 
        a dictionary. Each key in the dictionary corresponds to a tab name, and the 
        value is a list of records in JSON format.

        Raises:
            ValueError: If there is an issue loading the data (e.g., network issues, wrong URL).
        """
        try:
            xls = pd.ExcelFile(SheetManager.sheet_url)
            
            for sheet_name in xls.sheet_names:
                rows_data = pd.read_excel(xls, sheet_name)
                rows_data = json.loads(rows_data.to_json(orient='records'))
                
                SheetManager.sheet_data[sheet_name] = rows_data
        
        except Exception as e:
            raise ValueError(f"Error loading data from spreadsheet: {e}")
