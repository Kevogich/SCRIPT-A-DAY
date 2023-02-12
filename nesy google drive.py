from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

# Replace with your own credentials file
creds = service_account.Credentials.from_service_account_file('credentials.json')

# Connect to the Google Drive API
service = build('drive', 'v3', credentials=creds)

# Define the file metadata
file_metadata = {'name': f'nest_data_{datetime.date.today()}.txt'}

# Create the file on Google Drive
file = service.files().create(body=file_metadata, media_body='nest_data.txt', fields='id').execute()

# Print the ID of the file that was created
# print(f'File ID: {file.get("id")}')

from nest_thermostat_api import Nest

# Replace with your own Nest credentials
nest = Nest(username='USERNAME', password='PASSWORD')+
#TODO- Replace with AUTHID and SecretID

# Get the daily heating usage data
daily_usage = nest.get_daily_energy_usage()
