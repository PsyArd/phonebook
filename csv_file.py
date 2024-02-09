import csv

list_contacts = [{'last_name': 'Иванов', 'first_name': 'Иван', 'patronymic': 'Иванович', 'phone_number': '123',},
                 {'last_name': 'Петров', 'first_name': 'Иван', 'patronymic': 'Сергеевич', 'phone_number': '555',}]

with open('examle_file.csv', 'w', newline='', encoding='utf-8') as csv_file:
    # fieldnames = ['last_name', 'first_name', 'patronymic', 'phone_number']
    fieldnames = list_contacts[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_contacts)



# 'cp1251'
# 'cp-1251'
# f = open('myfile.txt', 'w', encoding='utf-8')
# f.write('какая-то строка\n')
# f.close()
#
# f = open('myfile.txt', 'a', encoding='utf-8')
# f.write('новая строка\n')
# f.close()

# with open('myfile.txt', 'w', encoding='utf-8') as fd:
#     fd.write('какая-то строка\n')

# with open('myfile.txt', 'r', encoding='utf-8') as fd:
#     from_file = fd.readlines()
#     print(from_file)
#
# with open('myfile2.txt', 'w', encoding='utf-8') as fd:
#     lines = ['строка\n', 'ещё строка\n', 'и ещё одна строчка\n']
#     fd.writelines(lines)
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)
# main.py
# FILE_NAME = 'phone_book.txt'
    
        # with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError as err:
    #     print('файла нет. Сначала введите данные\n')
    # else:
    #     print('else')
    # finally:
    #     print('finally')