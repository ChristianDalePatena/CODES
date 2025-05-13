import pyodbc


DRIVER_NAME = "SQL Server"
SERVER_NAME = "Christian"
DATABASE_NAME = "FARMERS_FARMERS"


connect = pyodbc.connect(
                    f'DRIVER={DRIVER_NAME};'
                    f'SERVER={SERVER_NAME};'
                    f'DATABASE={DATABASE_NAME};'
                    'Trusted_Connection=yes;'
                )


def SignUp(Role_type,Username,User_pass):
    try:
        cursor = connect.cursor()
        current_id = cursor.execute("SELECT MAX(User_Id) FROM Users").fetchone()[0]

        if current_id:
            id = current_id + 1
        else:
            id = 1000


        query_stmt = "INSERT INTO Users (User_Id,Role_type,Username,User_pass) VALUES (?,?,?,?)"
        cursor.execute(query_stmt,(id,Role_type,Username,User_pass))
        connect.commit()


    except pyodbc.Error as ex:
        print(f'Failed to create account {ex}')


def Login(user,password):

    try:
        cursor = connect.cursor()
        query_stmt = "SELECT * FROM Users WHERE Username = ? and User_pass = ?"
        USER = cursor.execute(query_stmt, (user, password)).fetchone()

        if USER:
            return USER


    except pyodbc.Error as ex:
        print(f'Failed to create account {ex}')
