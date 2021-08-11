from typing import Any, Union

from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build, Resource
import pprint
import io

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'mypython99-e3fcbad42298.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service: Union[Resource, Any] = build('drive', 'v3', credentials=credentials)

results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name, mimeType)").execute()
pp.pprint(results)

print(len(results.get('files')))

results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType, parents, createdTime, permissions, quotaBytesUsed)").execute()

pp.pprint(results.get('files')[1])

folder_id = '1FWv85je1k4g3o_TCMBHBcbJjmXEkB8i0'
name = 'gender_test.csv'
file_path = 'gender_test.csv'
file_metadata = {
                'name': name,
                'parents': [folder_id]
            }
media = MediaFileUpload(file_path, resumable=True)
r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
pp.pprint(r)








spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист номер один',
                               'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
}).execute()
spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)