from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import client, tools, file
from config import SCOPES, folder_id


def upload_file_in_drive(filename):

    store = file.Storage('credentials/google_token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials/googledrive_credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }

    media = MediaFileUpload('backup/'+filename, mimetype='application/json', resumable=False)

    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print("File ID :", uploaded_file.get('id'))
    # 'File ID: %s' % uploaded_file.get('id')


# upload_file_in_drive()
