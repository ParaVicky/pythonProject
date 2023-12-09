# локальный бот - фильмотека

from random import *

import json
films=[]
films.append("Matrix")
films.append("Solaris")
films.append("The Lord of the Rings")
films.append("The Texas Chainsaw Massacre")
films.append("Santa-Barbara")
def save():
    with open("films.json", "w", encoding="UTF-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Фильмотека успешно сохранена в файле films.json")

def load():
    with open("films.json", "r", encoding="UTF-8") as fh:
        films = json.load(fh)

    print("Фильмотека успешно загружена")

while True:
    command = input("Введите команду")

    if command == "/start":
        print("бот-фильмотека начал работу")

    elif command == "/stop":
        print("Бот завершил свою работу. Всего доброго и до новых встреч")
        break

    elif command == "/show all":
        print("Вот список фильмов: ")
        print(films)

    elif command == "/add":
        f = input("введите название фильма: ")
        films.append(f)
        print("Фильм был успешно добавлен")

    elif command == "/help":
        print("Ознакомьтесь со списком команд")

    elif command == "/delete":
        f = input("введите название фильма")
        if f in films:
            films.remove(f)
            print("Фильм был успешно удален")
        else:
            print("такого фильма нет")

    elif command == "/random":
        rnd = randint(0, len(films)-1)
        print("Слепой жребий предлагает фильм " + films[rnd])

    elif command == "/save":
        save()
    elif command == "/load":
        load()