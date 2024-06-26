import csv
import pandas as pd
import xml.etree.ElementTree as ET
from database_manager import Database


class DataImporter:
    @staticmethod
    def import_from_csv():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS books')
            cursor.execute(
                'CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100))')

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
            drop_query = 'DROP TABLE IF EXISTS books'
            create_query = 'CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100))'
            insert_query = 'INSERT INTO books (Name, Author) VALUES (?, ?)'
            select_query = 'SELECT * FROM books'

            cursor.execute(drop_query)
            cursor.execute(create_query)

            df = pd.read_excel('data/to_import.xlsx', engine='openpyxl')
            for _, row in df.iterrows():
                cursor.execute(insert_query, (row['Name'], row['Author']))

            print("Imported data from excel:")
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            conn.commit()

    @staticmethod
    def import_from_json():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            drop_query = 'DROP TABLE IF EXISTS books'
            create_query = 'CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100), Year INT, Pages INT)'
            insert_query = 'INSERT INTO books (Name, Author, Year, Pages) VALUES (?, ?, ?, ?)'
            select_query = 'SELECT * FROM books'

            cursor.execute(drop_query)
            cursor.execute(create_query)

            df = pd.read_json('data/to_import.json')
            for _, row in df.iterrows():
                cursor.execute(
                    insert_query, (row['Name'], row['Author'], row['Year'], row['Pages']))

            print("Imported data from json:")
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            conn.commit()

    @staticmethod
    def import_from_xml():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            drop_query = 'DROP TABLE IF EXISTS books'
            create_query = 'CREATE TABLE books (BookID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100), Author NVARCHAR(100), Year INT, Pages INT)'
            insert_query = 'INSERT INTO books (Name, Author, Year, Pages) VALUES (?, ?, ?, ?)'
            select_query = 'SELECT * FROM books'

            cursor.execute(drop_query)
            cursor.execute(create_query)

            tree = ET.parse('data/to_import.xml')
            root = tree.getroot()
            for book in root.findall('Book'):
                name = book.find('Name').text
                author = book.find('Author').text
                year = int(book.find('Year').text)
                pages = int(book.find('Pages').text)
                cursor.execute(insert_query, (name, author, year, pages))

            print("Imported data from XML:")
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            conn.commit()
