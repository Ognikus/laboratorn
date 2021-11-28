# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     "password": "",
#     "db_name": "labapy11",
#     'cursorclass': 'pymysql.cursors.DictCursor'
#
# }
#
# import pymysql
# from config import config
#
#
# try:
#     connection = pymysql.connect(
#         host=config['host'],
#         port=config['port'],
#         user=config['user'],
#         password=config['password'],
#         database=config['db_name'],
#
#     )
#     print('successfully connected...')
#     print('#'*20)
#
#     try:
#         with connection.cursor() as cursor:
#             name = input("Введите ФИО пользоватетя: ")
#             age_person = int(input('Введите возраст пользователя: '))
#             gender_person = input('Введите пол(мужской, женский): ')
#             id_posts = int(input('Выберите айди профессии: '))
#             id_company = int(input('Выберите айди компании: '))
#             insert_query = "INSERT INTO `person` (fio, age, gender, id_post, id_company) VALUES("+name+", "+int(age_person)+", "+gender_person+", "+int(id_posts)+", "+int(id_company)+")"
#             cursor.execute(connection, insert_query)
#             connection.commit()
#     finally:
#         connection.close()
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
