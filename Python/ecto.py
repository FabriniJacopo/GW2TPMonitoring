# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import json
import mysql
import mysql.connector
from datetime import datetime

#Connector info and authentication
mydb = mysql.connector.connect(
  host="localhost",
  user="youruser",
  password="yourpassword",
  database="yourDB"
)

#Function to print the json payload. Unused but can be useful.
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Change the code of the request with the item code you need
response = requests.get("https://api.guildwars2.com/v2/commerce/prices/19721")

#Uncomment to print the json response.
#jprint(response.json())

data = json.loads(response.content)

buys = data['buys']
sells = data['sells']

buyPrice = buys['unit_price']
sellPrice = sells['unit_price']

mycursor = mydb.cursor()

now = datetime.utcnow()

#Specify the table of your DB you want to write into
sql = "INSERT INTO ecto (buy, sell, date) VALUES (%s, %s, %s)"
val = (buyPrice, sellPrice, now.strftime('%Y-%m-%d %H:%M:%S'))
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")