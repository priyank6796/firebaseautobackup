# Firebase Auto Backup
Project helps you to take firebase backup to Google drive for free plan of firebase. It is running cron Job to take firebase backup in Google drive.
Firebase is not providing autoback of database for free plan

- Pre requirement to run the project
    * Firebase account with created project
    * Python version 3 or newer that this
    * Required python packages
        * firebase_admin
        * google-api-python-client 
        * oauth2client
        
- Steps to run this project
    
    * Download service_account json from firebase project setting and replace with 'credentials/firebase_service_key.json'
    * Drive API need to be enable to get google drive credential
    * Visit : https://developers.google.com/drive/api/v3/quickstart/python. Click on Enable the drive API
    * Download Credential JSON file to replace with 'credentials/googledrive_credentials.json' in project
    * Replace following configuration in 'config.py'
        * firebase_database_url
        * folder_id (Replace with your google drive folder id in which you want backup)
    * Run project(main.py) from PyCharm/console
    * Need to login into your google account in which you want backup
    * It will start backup into Google drive
    * Go and see, you get firebase backup in Google Drive folder
    
    