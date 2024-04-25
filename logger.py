
from datetime import datetime

def input_data():
    try:
        with open('Data.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines and lines[-5].strip():
                id = int(lines[-5].strip()) + 1
            else:
                id = 0
    except FileNotFoundError:
        id = 0
    
    noteTitle = input("Введите заголовок заметки: ")
    noteText = input("Введите текст заметки: ")
    noteTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Data.csv', 'a', encoding='utf-8') as file:
        file.write(
            f'{id}\n'
            f'{noteTitle}\n'
            f'{noteText}\n'
            f'{noteTime}\n\n')
    print("Данные успешно записаны")


def print_data():
    var = input ("Что бы увидеть заметки нажмите 1.\n"
                 "Для поиска по дате нажмите 2.\n"
                 "Ваш выбор: ")
    if var == '1':
        print("Ваши заметки:\n")
        with open('Data.csv', 'r', encoding= 'utf-8') as file:
            lines = file.readlines()
        for i in range(0, len(lines), 5):
            id = lines[i].strip()
            title = lines [i + 1].strip()
            text = lines [i + 2].strip()
            time = lines [i + 3].strip()
            print(f'ID: {id}')
            print(f'Заголовок: {title}')
            print(f'Текст: {text}')
            print(f'Время: {time}')
            print()
    elif var == '2':
        dataSearch = input("Ведите дату создания заметки в формате 'yyyy-mm-dd': ")
        print("Ваши заметки за" + dataSearch + ":\n")
        found = False
        with open('Data.csv', 'r', encoding= 'utf-8') as file:
            lines = file.readlines()
        for i in range(0, len(lines), 5):
            id = lines[i].strip()
            title = lines[i + 1].strip()
            text = lines[i + 2].strip()
            date_from_file = lines[i + 3].strip().split()[0]
            if date_from_file == dataSearch:
                found = True
                print(f'ID: {id}')
                print(f'Заголовок: {title}')
                print(f'Текст: {text}')
                print(f'Дата: {date_from_file}')
                print()
            if not found:
                print("Записи с указанной датой не найдены.")

    else:
        print("Ошибка! Выберите либо 1 либо 2")
        print_data()

def delete_data():
    idForDelete = input("Введите ID заметки которую хотите удалить: ")
    with open('Data.csv', 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    with open('Data.csv', 'w', encoding= 'utf-8') as file:
        found = False
        for i in range(0, len(lines), 5):
            id = lines[i].strip()
            title = lines[i + 1].strip()
            text = lines[i + 2].strip()
            date_from_file = lines[i + 3].strip().split()[0]
            if idForDelete == id:
                found = True
            else:
                file.write(f'{id}\n{title}\n{text}\n{date_from_file}\n\n')
        if not found:
            print("Записи с указанной датой не найдены.")
            print_data()

def edit_data():
    idForEdit = input("Введите ID заметки которую хотите редактировать: ")
    with open('Data.csv', 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    with open('Data.csv', 'w', encoding= 'utf-8') as file:
        found = False
        for i in range(0, len(lines), 5):
            id = lines[i].strip()
            title = lines[i + 1].strip()
            text = lines[i + 2].strip()
            date_from_file = lines[i + 3].strip().split()[0]
            if idForEdit == id:
                noteTitle = input("Введите заголовок заметки: ")
                noteText = input("Введите текст заметки: ")
                noteTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(
                    f'{id}\n'
                    f'{noteTitle}\n'
                    f'{noteText}\n'
                    f'{noteTime}\n\n')
                print("Данные успешно записаны")
                found = True
            else:
                file.write(f'{id}\n{title}\n{text}\n{date_from_file}\n\n')
        if not found:
            print("Заметка с указанным ID не найдена.")
