import json
with open('malpractice-detector-0e13defce47e.json') as f:
 data = json.load(f)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('malpractice-detector-0e13defce47e.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Sample_Db").sheet1
data = sheet.get_all_records()