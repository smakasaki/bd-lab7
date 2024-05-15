import signal
from database_manager import Database
from helper import Helper
from models import ClubRepository
from services import DataImporter, DataExporter


def main_menu():
    signal.signal(signal.SIGINT, Helper.signal_handler)
    Helper.delete_exported_files()

    while True:
        Helper.print_menu()
        choice = input("Введите номер действия: ")

        if choice == '1':
            Database.print_version()
        elif choice == '2':
            ClubRepository.create_table()
        elif choice == '3':
            ClubRepository.insert_data()
        elif choice == '4':
            ClubRepository.fetch_data()
        elif choice == '5':
            ClubRepository.update_data()
        elif choice == '6':
            ClubRepository.delete_data()
        elif choice == '7':
            ClubRepository.do_transaction()
        elif choice == '8':
            ClubRepository.handle_exception()
        elif choice == '9':
            DataExporter.export_to_csv()
            DataImporter.import_from_csv()
        elif choice == '10':
            DataExporter.export_to_excel()
            DataImporter.import_from_excel()
        elif choice == '11':
            DataExporter.export_to_json()
            DataImporter.import_from_json()
        elif choice == '12':
            DataExporter.export_to_xml()
            DataImporter.import_from_xml()
        elif choice == '0':
            print("Выход из программы...")
            Database.close_connection()
            break
        else:
            print("Неверный выбор. Пожалуйста, введите номер из списка.")


if __name__ == "__main__":
    main_menu()
