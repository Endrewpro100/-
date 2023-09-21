import requests
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect("sqlite.sl3")
cursor = connection.cursor()
response = requests.get("https://sinoptik.ua/погода-кременчуг")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.find(class_="today-temp")
    time = soup.find(class_="today-time")
    temperature = temp.get_text()
    current_time = time.get_text()
    cursor.execute("CREATE TABLE IF NOT EXISTS first_table (id INTEGER PRIMARY KEY, time TEXT, temperature TEXT)")
    cursor.execute("INSERT INTO first_table (time, temperature) VALUES (?, ?)", (current_time, temperature))
    connection.commit()
    connection.close()