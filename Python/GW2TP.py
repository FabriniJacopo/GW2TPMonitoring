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

#Table_name: Item_code
itemdict = {
  "saltandpepper": "12178",
  "ecto": "19721"
}

mycursor = mydb.cursor()
    
for item in itemdict:
    response = requests.get("https://api.guildwars2.com/v2/commerce/prices/" + itemdict[item])
    data = json.loads(response.content)
    
    buys = data['buys']
    sells = data['sells']

    buyPrice = buys['unit_price']
    sellPrice = sells['unit_price']    

    now = datetime.now()

    sql = "INSERT INTO " + item + " (buy, sell, date) VALUES (%s, %s, %s)"
    val = (buyPrice, sellPrice, now.strftime('%Y-%m-%d %H:%M:%S'))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")