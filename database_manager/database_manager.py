import pyodbc


class Database:
    conn = None

    @staticmethod
    def get_connection():
        if Database.conn is None:
            Database.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                'SERVER=WIN-8PDLU53VO2J;'
                'DATABASE=lab10;'
                'UID=python;'
                'PWD=python1337;'
                'TrustServerCertificate=yes;'
                'Encrypt=no;'
            )
        return Database.conn

    @staticmethod
    def close_connection():
        if Database.conn is not None:
            Database.conn.close()
            Database.conn = None

    @staticmethod
    def print_version():
        cursor = Database.get_connection().cursor()
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        print("Database version:", row[0])
