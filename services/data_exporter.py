from database_manager import Database
import csv
import pandas as pd
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

class DataExporter:
    @staticmethod
    def export_to_csv():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM professors')
            with open('data/professors.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([desc[0] for desc in cursor.description])  # Запись заголовков столбцов
                writer.writerows(cursor)
            print("Data exported to CSV")

    @staticmethod
    def export_to_excel():
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT Name, StudyGroup, IDNP, Age, Gender, PersonalEmail, EmergencyContact FROM students
                            JOIN student_info ON students.StudentID = student_info.StudentID;''')
            columns = [column[0] for column in cursor.description]
            data = cursor.fetchall()

            df = pd.DataFrame.from_records(data, columns=columns)
            
            # Сохранение DataFrame в Excel
            with pd.ExcelWriter('data/students.xlsx', engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Students')

                # Авто-растяжение столбцов и выравнивание контента по центру
                worksheet = writer.sheets['Students']

                center_aligned_text = Alignment(horizontal='center')
                for column in df:
                    col_idx = df.columns.get_loc(column) + 1
                    col_letter = get_column_letter(col_idx)
                    column_width = max(df[column].astype(str).map(len).max(), len(column)) + 2
                    worksheet.column_dimensions[col_letter].width = column_width

                    # Применение выравнивания по центру для каждой ячейки в столбце
                    for row in range(2, worksheet.max_row + 1):  # начинаем с 2, потому что 1-я строка - это заголовки
                        worksheet[f"{col_letter}{row}"].alignment = center_aligned_text

                print("Data exported to Excel")
