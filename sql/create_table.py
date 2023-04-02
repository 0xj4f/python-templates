import pyodbc
import settings

server = settings.server
database = settings.database
username = settings.username
password = settings.password
driver= settings.driver

def create_table():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin1')
        conn.setencoding('latin1')
        with conn.cursor() as cursor:
            cursor.execute("SELECT @@Version")
            row = cursor.fetchall()
            print(row)
            cursor.execute('''
            CREATE TABLE PeopleInfo (
                    PersonId INTEGER PRIMARY KEY,
                    FirstName TEXT NOT NULL,
                    LastName  TEXT NOT NULL,
                    Age INTEGER NULL,
            
            );

                        ''')
            print("Table Done")


if __name__ == "__main__":
    create_table()