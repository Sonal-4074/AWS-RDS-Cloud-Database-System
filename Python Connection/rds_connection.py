import mysql.connector

connection = mysql.connector.connect(
    host="interns-db.c5mqoguwsiar.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Sonal0105",
    database="InternshipDB"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM Interns")

for row in cursor.fetchall():
    print(row)

connection.close()