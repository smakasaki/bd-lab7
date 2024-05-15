from database_manager import Database


class ClubRepository:
    @staticmethod
    def create_table():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            query = '''
            DROP TABLE IF EXISTS clubs
            CREATE TABLE clubs (
                ClubID INT IDENTITY(1,1) PRIMARY KEY,
                Name NVARCHAR(100),
                Size INT,
                Location NVARCHAR(100),
                Founded DATE
            )
            '''
            cursor.execute(query)
            print("Table 'clubs' created")
            conn.commit()

    @staticmethod
    def insert_data():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO clubs (Name, Size, Location, Founded) VALUES (?, ?, ?, ?)'
            clubs = [
                ('Шахматный клуб', 100, 'Корпус А', '2012-01-01'),
                ('Баскетбольный клуб', 50, 'Корпус Б', '2013-05-02'),
                ('Клуб альпинизма', 200, 'Корпус Г', '2014-04-03')
            ]
            cursor.executemany(query, clubs)
            conn.commit()
            print("Inserted rows:\n" + str(clubs))

    @staticmethod
    def fetch_data():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clubs')
            rows = cursor.fetchall()
            print("Fetch all:")
            for row in rows:
                print(row)

            cursor.execute('SELECT * FROM clubs WHERE Size > 75')
            row = cursor.fetchone()
            print("Fetch one:")
            print(row)

    @staticmethod
    def update_data():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            select_query = 'SELECT * FROM clubs WHERE Name = ?'
            update_query = 'UPDATE clubs SET Size = 150 WHERE Name = ?'

            cursor.execute(update_query, 'Шахматный клуб')
            conn.commit()

            cursor.execute(select_query, 'Шахматный клуб')
            row = cursor.fetchone()
            print("Updated row:\n" + str(row))

    @staticmethod
    def delete_data():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            select_query = 'SELECT * FROM clubs'
            delete_query = 'DELETE FROM clubs WHERE Name = ?'

            cursor.execute(delete_query, 'Баскетбольный клуб')
            conn.commit()

            cursor.execute(select_query)
            rows = cursor.fetchall()
            print("After deletion:")
            for row in rows:
                print(row)

    @staticmethod
    def do_transaction():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            insert_query = 'INSERT INTO classrooms (Location, Capacity) VALUES (?, ?)'
            delete_query = 'DELETE FROM classrooms WHERE ID = ?'
            update_query = 'UPDATE clubs SET Size = 300 WHERE ClubID = ?'

            try:
                cursor.execute(insert_query, 'Основной корпус 322', 30)
                cursor.execute(delete_query, 2)
                cursor.execute(update_query, 1)
                conn.commit()
            except Exception as e:
                print("Transaction failed:", e)
                conn.rollback()

    @staticmethod
    def handle_exception():
        try:
            with Database.get_connection() as conn:
                cursor = conn.cursor()
                query = 'INSERT INTO classroom (ID, Location, Capacity) VALUES (1, "Blablabla", 50)'
                cursor.execute(query)
                conn.commit()
        except Exception as e:
            print("Exception:", e)
            conn.rollback()
