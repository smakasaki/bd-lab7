from database_manager import Database
import csv
import pandas as pd 

class DataImporter:
    @staticmethod
    def import_from_csv():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS books')
            cursor.execute('CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100))')

            with open('data/to_import.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cursor.execute('''
                        INSERT INTO books (Name, Author) VALUES (?, ?)
                    ''', (row['Name'], row['Author']))

            print("Imported data from csv:")
            cursor.execute('SELECT * FROM books')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
            conn.commit()

    @staticmethod
    def import_from_excel():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS books')
            cursor.execute('CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100))')

            df = pd.read_excel('data/to_import.xlsx', engine='openpyxl')
            for _, row in df.iterrows():
                cursor.execute('''
                    INSERT INTO books (Name, Author) VALUES (?, ?)
                ''', (row['Name'], row['Author']))

            print("Imported data from excel:")
            cursor.execute('SELECT * FROM books')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
            conn.commit()

    @staticmethod
    def import_from_json():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS books')
            cursor.execute('CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100), Year INT, Pages INT)')

            df = pd.read_json('data/books.json')
            for _, row in df.iterrows():
                cursor.execute('''
                    INSERT INTO books (Name, Author, Year, Pages) VALUES (?, ?, ?, ?)
                ''', (row['Name'], row['Author'], row['Year'], row['Pages']))

            print("Imported data from json:")
            cursor.execute('SELECT * FROM books')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
            conn.commit()