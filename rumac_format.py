import csv
import sqlite3


conn = sqlite3.connect("temp_perfil.db")
cur = conn.cursor()
cur.execute("SELECT temperature FROM rumac_test;")


data = cur.fetchall()

resultFile = open("data.csv", "wb")
wr = csv.writer(resultFile)
wr.writerows(data)
