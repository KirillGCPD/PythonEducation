import sqlite3 as sq
from prettytable import PrettyTable #py -m pip install PrettyTable библиотека для рисования табличек
from datetime import date

#название базы
db_name="phonebook.db"


#Печатаем всех. Если есть имя - будем искать по не точному совпадению. Если установлен флаг exactly в True то ищем один контакт
def print_all(name="",exactly=False):
    con = sq.connect(db_name)
    cursor = con.cursor()
    if name=="":
        cursor.execute("""select c.Name,c.Birthday,c.City,p.number,p.type from contacts c left join phone_numbers p on c.id = p.contact_id""")
    else:
        name=name.lower()
        if exactly: #Тут нужно точное совпадение, но мы все равно не учитываем регистр
            cursor.execute(f"select c.Name,c.Birthday,c.City,p.number,p.type from contacts c left join phone_numbers p on c.id = p.contact_id where c.Name_low_case = '{name}'")
        else:
            cursor.execute(f"select c.Name,c.Birthday,c.City,p.number,p.type from contacts c left join phone_numbers p on c.id = p.contact_id where c.Name_low_case like '%{name}%'")
    PTables = PrettyTable()
    PTables.field_names = ["Имя", "Дата рождения", "Город", "Телефон", "Тип"]
    PTables.add_rows(cursor.fetchall())
    print(PTables)
    con.close()


#Удалить контакт
def delete_contact(name):
    con = sq.connect(db_name)
    cursor = con.cursor()
    #в данных методах никаких проверки не требуются, если имени не будет в базе, то просто ничего не удалится
    cursor.execute("""DELETE FROM phone_numbers WHERE contact_id = (select id from contacts where name=?)""",[name]) #Сначала удаляем номера
    cursor.execute("""DELETE FROM contacts WHERE name=?""",[name]) #Теперь контакт
    con.commit()
    con.close()
#Удалить только 1 номер телефона
#требуется полное соотвествие
def delete_phone_number(phone_number):
    con = sq.connect(db_name)
    cursor = con.cursor()
    cursor.execute("""DELETE FROM phone_numbers WHERE nymber=?)""",[phone_number])
    con.commit()
    con.close()

def add_phone_number_to_contact(name):
    con = sq.connect(db_name)
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM contacts where name_low_case=?",[name.lower()])
    if len(cursor.fetchall())==0:
        print("Такого контакта не существует: ")
        prompt=input("Хотите сначала добавить контакт? Напишите да или нет: ")
        if prompt=="да":
            add_contact() #Тут алгоритм переплетается - он попытается добавить контакт и вновь вернется сюда
    else: #такой контакт есть
        print("Конакт найден, добавим к нему новый номер.")
        number=""
        number_type=""
        uniq=False
        while not uniq:
            number=input("Введите номер: ")
            number_type=input("Введите тип номера: ")
            cursor.execute("SELECT * FROM phone_numbers where number=?",[number])
            fetch=cursor.fetchall()
            if len(fetch)>0:
                uniq=False
                print("Номер не уникальный, повторите ввод.")
            else:
                uniq=True
        cursor.execute("""INSERT INTO phone_numbers VALUES (null,?,?, (SELECT contacts.id FROM contacts where name_low_case=?))""",[number,number_type,name.lower()])
        con.commit()
        print("Номер добавился!")
    con.close()

def add_contact():
    con = sq.connect(db_name)
    cursor = con.cursor()
    
    name=input("Введите фио контакта: ")

    cursor.execute("SELECT * FROM contacts where name_low_case=?",[name.lower()])
    if (len(cursor.fetchall())>0):
        print("Такой контакт уже существует: ")
        print_all(name,True)
        prompt=input("Хотите добавить к нему номер? Напишите да или нет: ")
        if prompt=="да":
            add_phone_number_to_contact(name)
    else:
        prompt=input("Конакт отсутствует в списке. Хотите его создать? Напишите да: ")
        if prompt=="да":
            birthday=get_birthday()
            city=input("Введите город: ")
            if city=="":
                city=None
            cursor.execute("""INSERT INTO contacts VALUES (null,?,?,?,?)""",[name,name.lower(),birthday,city])
            con.commit()
            print(f"Отлично {name} добавлен!")
            prompt=input("Хотите добавить к нему номер? Напишите да или нет: ")
            if prompt=="да":
                add_phone_number_to_contact(name)
    con.close()

def edit_contact():
    con = sq.connect(db_name)
    cursor = con.cursor()
    
    name=input("Введите фио контакта: ")

    cursor.execute("SELECT * FROM contacts where name_low_case=?",[name.lower()])
    if (len(cursor.fetchall())>0):
        print("Такой контакт существует: ")
        print_all(name,True)
        prompt=input("Хотите его изменить? Напишите да или нет: ")
        if prompt=="да":
            old_name=name

            unique=False
            while not unique:
                name=input("Введите новое имя: ")
                if (old_name==name):
                    unique=True
                    break
                cursor.execute("SELECT * FROM contacts where name_low_case=?",[name.lower()])
                fetch=cursor.fetchall()
                if len(fetch)>0: #тут больше одного потому что одно оно уже такое есть и мы его меняем
                    unique=False
                    print("Имя не уникальное, повторите ввод.")
                else:
                    unique=True
            birthday=get_birthday()
            city=input("Введите город: ")
            if city=="":
                city=None
            cursor.execute("""UPDATE contacts SET name=?,name_low_case=?,birthday=?,city=? where name_low_case=?""",[name,name.lower(),birthday,city,old_name])
            con.commit()
            print(f"Отлично {name} добавлен!")
            prompt=input("Хотите добавить к нему номер? Напишите да или нет: ")
            if prompt=="да":
                add_phone_number_to_contact(name)
    else:
        print("Такого контакта не существует")
    con.close()

#Получить дату рождения, если не получится то будет пусто
def get_birthday():
    date_text=input("Введите дату рождения в формате dd.mm.yyyy, если введете не корретные данные то дата останется пустой: ")
    try:
        date_components = date_text.split(".")
        day, month, year = [int(item) for item in date_components]
        d = date(year, month, day)
        return date_text
    except:
        return None
#Перезапонить полностью телефонную базу изначальными данными
def reset_phone_base():
    con = sq.connect(db_name)
    cursor = con.cursor()
    #На этот момент таблицы уже созданы
    #Заполняем предварительными данными Очищаем
    cursor.execute("""DELETE FROM phone_numbers""")
    cursor.execute("""DELETE FROM contacts""")
    con.commit()
    #Чтоб не перечислять поля null первое для автоинкремента просто оставит автоинкермент
    cursor.execute("""INSERT INTO contacts VALUES (null,'Жанна Олеговна','жанна олеговна', '24.02.1978','Москва')""")
    cursor.execute("""INSERT INTO contacts VALUES (null,'Виталий Сантехник','виталий сантехник', null,'Ростов')""")
    cursor.execute("""INSERT INTO contacts VALUES (null,'Мама','мама', '24.02.1965','Ростов')""")
    cursor.execute("""INSERT INTO contacts VALUES (null,'Забыл Добавить Номер','забыл добавить номер', '25.08.1998','Ростов')""") #У контакта может не быть номеров, добавили только дату
    #Подзапросом определеям id Жанны и т.д.
    cursor.execute("""INSERT INTO phone_numbers VALUES (null,'+79856545522','рабочий', (SELECT contacts.id FROM contacts where Name='Жанна Олеговна'))""")
    cursor.execute("""INSERT INTO phone_numbers VALUES (null,'8800553535','рабочий', (SELECT contacts.id FROM contacts where Name='Виталий Сантехник'))""")
    cursor.execute("""INSERT INTO phone_numbers VALUES (null,'+73855566352','домашний', (SELECT contacts.id FROM contacts where Name='Мама'))""")
    cursor.execute("""INSERT INTO phone_numbers VALUES (null,'+79086654555','рабочий', (SELECT contacts.id FROM contacts where Name='Мама'))""")
    con.commit()
    con.close()

#предварительно создадим пустую базу
con = sq.connect(db_name)
cursor = con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
  id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  name     varchar(255) UNIQUE, 
  name_low_case varchar(255) UNIQUE, 
  birthday date, 
  city     varchar(255));
""") #В пайтон sqllite нельзя выполнять два выражения в одном запросе, вторую таблицу создаем отдельно
cursor.execute("""
CREATE TABLE IF NOT EXISTS phone_numbers (
  id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  number     varchar(255) UNIQUE, 
  type       varchar(255), 
  contact_id integer(10) NOT NULL, 
  FOREIGN KEY(contact_id) REFERENCES contacts(id));
""")
con.close()


while (True):
    print("""Список команд: 
    /all или просто *: распечатает справочник
    /search часть_имени: гибкий поиск по справочнику
    /lorem: перезаполнит справочник предварительными данными
    /delete_contact: удаляет контакт вместе с телефонами
    /delete_phone: удаляет телефон
    /add: Универсальная команда добавления. Сначала вводите имя контакта, если он есть в списке, 
        то будет предложено доавбить номер, а если в списке контакта нет, то будет предложено создать его
    /edit: изменить контакт. Изменить номер нельзя, так как его можно просто удалить и добавить новый
    /q - выход""")
    command=input('Введите команду: ')
    if command=="/all" or command=="*":
        print('Список всех номеров: ')
        print_all()
    elif command.startswith("/search"):
        print(f"Поиск по части имени {command[8:]}:")
        print_all(command[8:])
    elif command=="/lorem":
        prompt=input("Данная команда удалит все данные и заполнить базу своими, если вы уверены напишите да: ")
        if prompt=="да":
            reset_phone_base()
    elif command=="/delete_contact":
        contact_name=input("Введите точное имя контакта который хотите удалить: ")
        prompt=input(f"Данная команда так же удалит и номера у контакта {contact_name}, если хотите продожить напишите да:")
        if prompt=="да":
            delete_contact(contact_name)
    elif command=="/delete_phone":
        phone_number=input("Введите точный номер телефона для удаления: ")
        delete_phone_number(phone_number)
    elif command=="/add":
        add_contact()
    elif command=="/edit":
        edit_contact()
    elif command=="/q":
        break