import mysql.connector

mydb = mysql.connector.connect(
  host="172.31.18.86",
  user="root",
  password="Emily123$",
  database="Northwind"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0] + ", " + x[1])