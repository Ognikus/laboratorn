matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
          [8, 7, 6, 5, 4, 3, 2, 1],
          [2, 3, 4, 5, 6, 7, 8, 9],
          [9, 8, 7, 6, 5, 4, 3, 2],
          [1, 3, 5, 7, 9, 7, 5, 3],
          [3, 1, 5, 3, 2, 6, 5, 7],
          [1, 7, 5, 9, 7, 3, 1, 5],
          [2, 6, 3, 5, 1, 7, 3, 2],]


def matrix_del_stroka():
    print("Оригинальная матрица", *matrix, sep="\n", end="\n\n")
    r = int(input('Какую строку удалить? '))
    matrix.pop(r-1)
    for i in range(7):
        print(matrix[i])

def matrix_del_stolb():
    print("Оригинальная матрица", *matrix, sep="\n", end="\n\n")
    k = int(input('Какой столбец удалить? '))
    for i in matrix:
        i.pop(k- 1)
    for i in range(8):
        print(matrix[i])

def matrix_clear():
    print("Оригинальная матрица", *matrix, sep="\n", end="\n\n")
    matrix.clear()
    print(matrix)

def reverse():
    print("Оригинальная матрица", *matrix, sep="\n", end="\n\n")
    b = matrix[0]
    matrix[0] = matrix[-1]
    matrix[-1] = b
    print(*matrix, sep="\n", end="\n\n")

while True:
    b = int(input("Выберите функцию:\n0 - Закончить программу;\n1 - Удалить строку в матрицу;\n2 - Удалить столбец в матрице;\n3 - Очистить матрицу;\n4 - Поменять первы и последний столбцы матрицы;\nВведите номер: "))
    if b == 0:
        break
    elif b == 1:
        matrix_del_stroka()
    elif b == 2:
        matrix_del_stolb()
    elif b == 3:
        matrix_clear()
    elif b == 4:
        reverse()
    else:
        print("Некоректный ввод")
    print("Если желаете продолжить введите: Да, 1, Yes\nЕсли желаете закончить введите: Нет, 0, No ")
    c = input('Вы хотите продолжить?: ')
    if c == 'Да' or c == '1' or c == "Yes" or c == 'да' or c == 'yes':
        continue
    elif c == 'Нет' or c == '0' or c == "No" or c == 'нет' or c == 'no':
        break
    else:
        print('Некорректный ввод')


