# Set up your imports and your flask app.
from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# This page will be the page after the form
@app.route('/report')
def report():
   lower_letter = False
   upper_letter = False
   num_end = False
   username = request.args.get('username')
   lower_letter = any(c.islower() for c in username)
   upper_letter = any(c.isupper() for c in username)
   num_end = username[-1].isdigit()
   report = lower_letter and upper_letter and num_end
   return render_template('report.html', report=report, lower=lower_letter, upper=upper_letter, num_end=num_end)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

mydb = mysql.connector.connect(
  host="172.31.26.182",
  user="root",
  password="Emily123$",
  database="Northwind"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)