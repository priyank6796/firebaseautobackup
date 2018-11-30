from firebase import get_firebase_data
import datetime
from fileoperation import write_data_backup
from google_drive import upload_file_in_drive

print("Start backup of firebase real-time db")
data = get_firebase_data()
now = datetime.datetime.now()
filename = str(now.strftime("%Y-%m-%d")) + '.json'
write_data_backup(filename, data)

upload_file_in_drive(filename)
print("end backup of firebase real-time db")
