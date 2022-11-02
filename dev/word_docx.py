import os
import time
from datetime import date

from docx import Document

from .password import PASSWORD


def create_word_file(username: str, userpassword: str, email: str, discript: str, ) -> int:
    """Создаем Word файл"""
    docx_name = username + '_' + str(date.today())
    os.system(
        f'copy \\\\miacshare\\mailzdrav$\\Готовые\\Template.docx \\\\miacshare\\mailzdrav$\\Готовые\\{docx_name}.docx')
    doc = Document(f'\\\\miacshare\\mailzdrav$\\Готовые\\{docx_name}.docx')
    # добавляем таблицу 2x4
    table = doc.add_table(rows=2, cols=4)
    # применяем стиль для таблицы
    table.style = 'Table Grid'

    cell = table.cell(0, 0)  # rows , cols
    cell.text = "UserName"
    cell = table.cell(0, 1)
    cell.text = "UserPassword"
    cell = table.cell(0, 2)
    cell.text = "Email"
    cell = table.cell(0, 3)
    cell.text = "Discription"

    cell = table.cell(1, 0)
    cell.text = '\n' + username + '\n'
    cell = table.cell(1, 1)
    cell.text = '\n' + userpassword + '\n'
    cell = table.cell(1, 2)
    cell.text = '\n' + email + '\n'
    cell = table.cell(1, 3)
    cell.text = '\n' + discript + '\n'

    doc.save(f'\\\\miacshare\\mailzdrav$\\Готовые\\{docx_name}.docx')

    time.sleep(1)

    # Архивируем
    os.system(f"\"C:\Program Files\\7-Zip\\7z.exe\" a -tzip -mx=0 -p{PASSWORD} \\\\miacshare\\mailzdrav$\\Готовые\\{docx_name}.zip \\\\miacshare\\mailzdrav$\\Готовые\\{docx_name}.docx")



