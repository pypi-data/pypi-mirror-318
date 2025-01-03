import json
import dbutils
import gspread
import pandas as pd
import datetime as dt

from google.oauth2.service_account import Credentials

class GSheetHelper:
    # Constructor
    def __init__(self, sheet_id, scope="team-offprice-market-analytics-scope", key="bq_credential"):
        """
        Initializes the GSheetHelper with the given Google Sheet id
        """
        # Read credentials from secret store and translate them into JSON format
        credentials = dbutils.secrets.get(scope=scope, key=key)
        service_account = json.loads(credentials)

        # Define the scope and authorize using the credentials file
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_info(service_account, scopes=scopes)

        # Connect to Google Sheets API and access the Google Sheet by id
        client = gspread.authorize(creds)
        self.__spreadsheet__ = client.open_by_key(sheet_id)

    # Read Cell
    def __read_cell__(self, worksheet_name, cell):
        """
            Reads the given cell from the given sheet.
        """
        worksheet = self.__spreadsheet__.worksheet(worksheet_name)
        return worksheet.acell(cell).value

    # Read Range
    def __read_range__(self, worksheet_name, cell_range, header=True, header_range=None):
        """
            Reads the given range from the given sheet.
        """
        sheet = self.__spreadsheet__.worksheet(worksheet_name)
        values = sheet.get_values(cell_range)

        # If header is not defined then take the first row as header
        # Otherwise, take the defined range as header
        if header:
            if header_range is None:
                header = values[0]
                values = values[1:]
            else:
                header = sheet.get_values(header_range)[0]

            df = pd.DataFrame(values, columns=header)
        # If no header is defined then return pd.DataFrame without any header information
        else:
            df = pd.DataFrame(values)

        return df
    
    # Write Cell
    def __write_cell__(self, worksheet_name, value, cell):
        """
            Writes the given value to the given cell in the given sheet.
        """
        worksheet = self.__spreadsheet__.worksheet(worksheet_name)
        worksheet.update_acell(cell, value)

    # Write Dataframe
    def __write_dataframe__(self, worksheet_name, df, start_cell, header=True):
        """
            Writes the given DataFrame to the given cell in the given sheet.
        """
        worksheet = self.__spreadsheet__.worksheet(worksheet_name)

        # Convert DataFrame to a 2D list, including header if specified
        data = [df.columns.tolist()] + df.values.tolist() if header else df.values.tolist()
        worksheet.update(start_cell, data)
    
    # Read
    def read(self, worksheet_name, cell_or_range, header=True, header_range=None, log=True):
        """
            Reads the given cell or range from the given sheet.
        """
        if log: print(f"[{dt.datetime.now()}] Reading {cell_or_range} from Tab: {worksheet_name}")

        if ':' in cell_or_range:
            range = cell_or_range
            return self.__read_range__(worksheet_name, range, header, header_range)
        
        cell = cell_or_range
        return self.__read_cell__(worksheet_name, cell)

    # Write
    def write(self, worksheet_name, val_or_df, cell, log=True):
        """
            Writes the given value or DataFrame to the given cell in the given sheet.
        """
        if log: print(f"[{dt.datetime.now()}] Writing at {cell} to Tab: {worksheet_name}")

        if isinstance(val_or_df, pd.DataFrame):
            df = val_or_df
            self.__write_dataframe__(worksheet_name, df, cell)
        else:
            val = val_or_df
            self.__write_cell__(worksheet_name, val, cell)

    # Delete
    def delete(self, worksheet_name, cell_or_range, log=True):
        """
            Deletes the given cell or range from the given sheet.
        """
        if log: print(f"[{dt.datetime.now()}] Deleting {cell_or_range} from Tab: {worksheet_name}")

        worksheet = self.__spreadsheet__.worksheet(worksheet_name)

        if ':' in cell_or_range:
            range = cell_or_range
            range_data = worksheet.get_values(range)
            empty_values = [['' for _ in row] for row in range_data]
            self.__write_dataframe__(worksheet_name, pd.DataFrame(empty_values), range.split(":")[0], False)
        else:
            cell = cell_or_range
            self.__write_cell__(worksheet_name, '', cell)