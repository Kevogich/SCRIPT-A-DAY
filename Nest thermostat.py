import nest
import time
import sqlite3
import datetime

napi = nest.Nest(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
device = napi.devices[0]
current_temperature = device.temperature
current_humidity = device.humidity

conn = sqlite3.connect('heating_data.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS heating_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    temperature REAL NOT NULL
)
''')

current_temperature = 20.5 # Example temperature
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO heating_data (date, temperature) VALUES (?, ?)", (now, current_temperature))
conn.commit()
conn.close()
