import pyodbc
import settings

server = settings.server
database = settings.database
username = settings.username
password = settings.password
driver= settings.driver


def insert_data():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin1')
        conn.setencoding('latin1')
        with conn.cursor() as cursor:
            cursor.execute("SELECT @@Version")
            row = cursor.fetchall()
            print(row)
        cursor.execute('''
                INSERT INTO PeopleInfo (PersonId, FirstName, LastName, Age)
                VALUES
                (1, 'Tasteless','Degenerate', 25),
                (2, 'Ms','Derpette', 25),
                (3, 'Gilfolye','Bertram', 25),
                (4, 'Dinesh','Chugtai', 25),
                (5, 'Sam','Sepiol', 25),
                (6, 'Elliot','Alderson', 25),
                (7, 'Tyrell','Wellick', 25)

                ''')

if __name__ == "__main__":
    insert_data()
