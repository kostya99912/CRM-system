import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost' , 
    user = 'root' ,
    password = '' , 
)

cursorObject = dataBase.cursor()


#Creating a database 
cursorObject.execute("CREATE DATABASE dcrmdb")

print("All done!")