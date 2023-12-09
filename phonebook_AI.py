import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы для хранения контактов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT
    )
''')

# Функция для добавления нового контакта
def add_contact(name, phone):
    cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()

# Функция для поиска контакта по имени
def find_contact(name):
    cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
    return cursor.fetchone()

# Функция для обновления контакта по имени
def update_contact(name, new_phone):
    cursor.execute('UPDATE contacts SET phone = ? WHERE name = ?', (new_phone, name))
    conn.commit()

# Функция для удаления контакта по имени
def delete_contact(name):
    cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
    conn.commit()

# Функция для просмотра всех контактов
def view_contacts():
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()

# Пример использования функций
add_contact('Иван', '12345')
add_contact('Мария', '54321')
print(find_contact('Иван'))
update_contact('Иван', '11111')
print(view_contacts())
delete_contact('Мария')
print(view_contacts())

# Закрытие соединения с базой данных
conn.close()