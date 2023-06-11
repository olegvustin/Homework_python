import csv

PHONEBOOK_FILE = 'PhoneBook.txt'

def load_phonebook():
    phonebook = []
    with open(PHONEBOOK_FILE, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            phonebook.append(row)
    return phonebook

def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(phonebook)

def print_phonebook(phonebook):
    for record in phonebook:
        print('Фамилия:', record[0])
        print('Имя:', record[1])
        print('Отчество:', record[2])
        print('Номер телефона:', record[3])
        print('------------------------------')

def search_phonebook(phonebook, query):
    results = []
    for record in phonebook:
        if query.lower() in record[0].lower() or query.lower() in record[1].lower() or query.lower() in record[2].lower():
            results.append(record)
    return results

def add_record(phonebook):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_record = [last_name, first_name, middle_name, phone_number]
    phonebook.append(new_record)
    save_phonebook(phonebook)
    print('Запись добавлена успешно.')

def menu():
    phonebook = load_phonebook()
    while True:
        print('==== Телефонный справочник ====')
        print('1. Вывести все записи')
        print('2. Поиск записей')
        print('3. Добавить запись')
        print('0. Выйти')
        choice = input('Введите номер действия: ')
        print()
        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            query = input('Введите фамилию, имя или отчество для поиска: ')
            results = search_phonebook(phonebook, query)
            if results:
                print('Результаты поиска:')
                print_phonebook(results)
            else:
                print('Нет совпадений.')
        elif choice == '3':
            add_record(phonebook)
        elif choice == '0':
            break
        else:
            print('Неверный выбор. Пожалуйста, повторите.')

menu()