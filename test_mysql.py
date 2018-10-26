import requests
import json
import mysql.connector
from pprint import pprint

# specify your database
db = 'YOUR_DATABASE'

# create your connection and cursor
mysql = mysql.connector.connect(
    user = 'YOUR_SQL_USER',
    password = 'YOUR_SQL_PASSWORD',
    host = 'your.db.hostname.com') # or IP 

cursor = mysql.cursor()

# select the database
cursor.execute(f'USE {db}')

# execute 'SHOW TABLES'
cursor.execute('SHOW TABLES')

# iterate over the return and print table names on separate lines
for (table_name,) in cursor:
    print(table_name)