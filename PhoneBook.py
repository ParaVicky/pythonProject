# локальный бот - фильмотека

from random import *

import json
phonebook={"Иван Сергеевич Тургенев" : {'phones':[1234567, 7456321], 'email':'vano@mumu.ru', 'birtday': '28.10.1818'},\
           "Михаил Афанасьевич Булгаков":{'phones':[9876541], 'email':'voland@ya.ru', 'birthday': '15.05.1891'},\
           "Серега Есенин":{'phones':[9852645]}\
           }

#print(phonebook['Серега Есенин']['phones'])
def save():
    with open("phonebook.json", "w", encoding="UTF-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Ваша телефонная книга успешно сохранена в файле phonebook.json")

def load():
    with open("phonebook.json", "r", encoding="UTF-8") as fh:
        phonebook = json.load(fh)
    print("Ваша телефонная книга успешно загружена")

# def new():
    # name = input('Введите имя контакта')
    # phone = input('Введите номера телефонов через запятую').split()
    # email = input('Введите адрес электронной почты, если есть')
    # birthday = input('Введите день рождения контакта, если есть, или поставьте прочерк')
    # if '@' in email:
    #     phonebook[name] = {'phones':phone, 'email':email, 'birthday':birthday}
    # else:
    #     phonebook[name] = {'phones': phone, 'birthday': birthday}

while True:
    command = input("Введите команду: ")

    if command == "/start":
        print("Ваша телефонная книга открыта")

    elif command == "/stop":
        print("Ваша телефонная книга закрыта. Всего доброго и до новых встреч")
        break

    elif command == "/show all":
        print("Вот ваши сохраненные контакты: ")
        print(phonebook.keys())

    elif command == "/add":
        name = input('Введите имя контакта: ')
        phone = input('Введите номера телефонов через запятую: ').split()
        email = input('Введите адрес электронной почты, если есть: ')
        birthday = input('Введите день рождения контакта, если есть, или поставьте прочерк: ')
        if '@' in email:
            phonebook[name] = {'phones': phone, 'email': email, 'birthday': birthday}
        else:
            phonebook[name] = {'phones': phone, 'birthday': birthday}

    elif command == "/delete":
        f = input("введите имя контакта: ")
        if f in phonebook:
            del phonebook[f]
            print("Контакт был успешно удален")
        else:
            print("такого контакта нет в вашей книге")
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    elif command == "/edit name":
        f = input("Введите имя контакта, который вы хотите изменить: ")
        h = input("Введите новое имя контакта: ")
        phonebook[h] = phonebook.pop(f)
        print(phonebook)

    # elif command == "/edit info":
    #     f = input("Введите имя контакта, данные которого вы хотите изменить: ")
    #     print(phonebook[f])
    #     h = input("Введите данные, которые вы хотите изменить: ")
    #     if h == 'телефон':
    #         new_phone = input('введите новый номер: ')
    #         phonebook['phones'] = new_phone
    #     elif h == 'email':
    #         new_email = input('введите новый адрес электронной почты: ')
    #         phonebook['email'] = new_email
    #     elif h == 'ДР':
    #         new_birthday = input('введите новую дату рождения: ')
    #         phonebook['birthday'] = new_birthday
    #     print(phonebook[f])

    else:
        print("Неизвестная команда. Попробуйте еще раз")



