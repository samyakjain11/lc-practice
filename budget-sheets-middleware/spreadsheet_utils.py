from google.oauth2 import service_account
from googleapiclient.discovery import build

email = 'master@civic-circuit-374303.iam.gserviceaccount.com'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def insert_row(spreadsheet_id, num_rows, values, num_fields):
    sheet = build('sheets', 'v4', credentials=creds).spreadsheets()
    sheet.values().update(
        spreadsheetId = spreadsheet_id,
        valueInputOption = 'USER_ENTERED',
        range = f'A{int(num_rows) + 1}:{chr(64 + num_fields)}{int(num_rows)+2}',
        body = {'values':values}
    ).execute()
    
