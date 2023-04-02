import pyodbc
import settings

server = settings.server
database = settings.database
username = settings.username
password = settings.password
driver= settings.driver

def query_records():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin1')
        conn.setencoding('latin1')
        with conn.cursor() as cursor:
            cursor.execute("SELECT @@Version")
            row = cursor.fetchall()
            print(row)

        cursor.execute('SELECT * FROM PeopleInfo')
        for row in cursor:
            print(row)

if __name__ == "__main__":
    query_records()
