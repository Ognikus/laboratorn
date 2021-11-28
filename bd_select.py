import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='labapy11'
)

#Создание новой должности
def new_post():
    mycursor = mydb.cursor()
    sqlFormula = 'INSERT INTO post(name post) VALUES(%s)'
    name_new_post = input('Введите название должности: ')
    post1 = (name_new_post)
    mycursor.execute(sqlFormula, post1)
    mydb.commit()
#Создание новой компании
def new_company():
    mycursor = mydb.cursor()
    sqlFormula = 'INSERT INTO firm(company) VALUES(%s)'
    name_new_firm = input('Введите название компании: ')
    company1 =(name_new_firm)
    mycursor.execute(sqlFormula, company1)
    mydb.commit()
#Создание нового пользователя
def new_user():
    mycursor = mydb.cursor()
    sqlFormula = 'INSERT INTO person(fio, age, gender, id_post, id_company) VALUES(%s, %s, %s, %s, %s)'
    last_name = input('Введите ФИО: ')
    age_person = int(input('Введите возраст: '))
    gender_person = input('Введите пол: ')
    id_post_person = int(input('Введите айди специальности: '))
    id_company_person = int(input('Введите айди компании: '))
    user1 = (last_name, age_person, gender_person, id_post_person, id_company_person)

    mycursor.execute(sqlFormula, user1)
    mydb.commit()
#Вывод всех компаний
def list_companies():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM firm')
    my_result = mycursor.fetchall()

    for row in my_result:
        print(*row)
#Вывод всех профессий
def list_posts():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM post')
    my_result = mycursor.fetchall()

    for row in my_result:
        print(*row)
#Вывод всех пользователей
def conclusion():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT person.`fio`, `age`, `gender`, post.`name post`, firm.`company`\
     FROM `person` person, `post` post, `firm` firm\
     WHERE person.`id_post` = post.`id` AND person.`id_company` = firm.`id`')
    my_result = mycursor.fetchall()

    for row in my_result:
        print(row)

conclusion()