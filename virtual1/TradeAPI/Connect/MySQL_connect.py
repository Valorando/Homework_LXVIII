import os
import json
import mysql.connector

connection_data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TradeAPI', 'Configuration_files', 'Connection_string.json'))
sql_requests_data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'TradeAPI', 'Configuration_files', 'Sql_requests.json'))

with open(connection_data_file, 'r') as file:
    connect_data = json.load(file)

with open(sql_requests_data_file, 'r') as file:
    requests_data = json.load(file)

db = mysql.connector.connect(
    host=connect_data['Host'],
    user=connect_data['User'],
    password=connect_data['Password'],
    database=connect_data['Database']
)

cursor = db.cursor()