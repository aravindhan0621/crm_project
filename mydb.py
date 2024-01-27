import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Avi@123456'

)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crm_database")
print('database created sucessfulley')