import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Oluwafemi1.",
    database="newfem"
)

print(mydb.get_server_info())


mycursor = mydb.cursor()


mycursor.execute("""
CREATE TABLE IF NOT EXISTS books(
   id INT AUTO_INCREMENT PRIMARY KEY,
   title VARCHAR(255) NOT NULL,
   author VARCHAR(255) NOT NULL,
   ISBN VARCHAR(255) NOT NULL
)
""")
"""
sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
val = ("Salt", "Ruth Abe", "134-6765")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "row(s) inserted")

val = ("Art", "Ade Thompson", "546-8765")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "row(s) inserted")

val = ("Aid", "Eben Joke", "123-0987")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "row(s) inserted")
"""
mycursor.execute("SELECT * FROM books")
myresult = mycursor.fetchall()
for book in myresult:
    print(book)

mycursor.execute("SELECT * FROM books WHERE title = 'Art'")
myresult = mycursor.fetchone()
print(myresult)

mycursor.fetchall()

sql = "DELETE FROM books WHERE id = %s"
val = (1,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "row(s) deleted")

mycursor.close()
mydb.close()

print("database connection close")
