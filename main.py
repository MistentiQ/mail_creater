import os

import PySimpleGUI as sg
import pyperclip

from dev import *

sg.theme('DarkGrey8')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Добавление нового пользователя ZdravMail')],
            [sg.Text('Имя пользователя')],
            [sg.InputText(key='Username')],
            [sg.Text('Пароль')],
            [sg.InputText(key='Pass')],
            [sg.Text('Описание')],
            [sg.InputText(key='Dis')],
            [sg.Text('')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Window Title', layout)

def main():
    while True:
        event, values = window.read()
        username = values['Username']
        userpassword = values['Pass']
        email = str(values['Username'])+"@zdrav.spb.ru"
        discript = values['Dis']

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        # Пишем Excel
        write_excel(username, userpassword, email, discript)
        # Создаём док для выдачи
        create_word_file(username, userpassword, email, discript)
        # Заносим юзверя в базу
        adduser_mssql(username, userpassword, email, discript)
        # Говорим пользователю что у нас всё получилось
        pyperclip.copy(PASSWORD) # закидываем пароль в буфер обмена
        sg.popup("Пароль пользователя: ", PASSWORD, '\n', "Пароль скопирован!")

        window.close()
        os.system("explorer \\\\miacshare\\mailzdrav$\\Готовые")

if __name__ == "__main__":
    main()
