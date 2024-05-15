import os
import sys
from database_manager import Database


class Helper:
    @staticmethod
    def signal_handler():
        print('\nВыход из программы... (Ctrl+C)')
        Database.close_connection()
        sys.exit(0)

    @staticmethod
    def delete_exported_files():
        directory = 'data'
        files_to_delete = ['students.csv', 'students.xlsx',
                           'students.xml', 'students.json']

        for file_name in files_to_delete:
            file_path = os.path.join(directory, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Файл {file_path} успешно удален.")
            else:
                print(f"Файл {file_path} не найден.")

    @staticmethod
    def print_menu():
        print("\nВыберите действие:")
        print("1 - Показать версию сервера базы данных")
        print("2 - Создать таблицу клубов")
        print("3 - Вставить данные в таблицу клубов")
        print("4 - Вывести данные таблицы клубов")
        print("5 - Обновить данные клубов")
        print("6 - Удалить данные из таблицы клубов")
        print("7 - Выполнить транзакцию с возможным откатом")
        print("8 - Обработка исключений при вставке данных")
        print("9 - Экспорт/Импорт данных в/из CSV")
        print("10 - Экспорт/Импорт данных в/из Excel")
        print("11 - Экспорт/Импорт данных в/из JSON")
        print("12 - Экспорт/Импорт данных в/из XML")
        print("0 - Выход\n")
