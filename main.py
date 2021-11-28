spisok = [[1, 'Макаров Иван Максимович', 18, 'ВУС21'],[2, 'Пелипченко Роман Иванович', 24, 'СУП41'],
          [3, 'Рыков Илья Николаевич', 26, 'ВП22'], [4, 'Сурков Николай Николаевич', 22, 'ВУС22'],
          [5, 'Рам Рина Васильевна', 21, 'СУП31'], [6, 'Баранова Алиса Станиславовна',19,'ВИ-33']]

slovar = {x[0]: x[1:] for x in spisok}

print(slovar)
b = int(input('Выберите задание(1, 2): '))

print('_' * 30)
if b == 1:
    for i in slovar:
        if slovar[i][1]>22:
            slovar[i][1] -=1
    print(slovar)

if b == 2:
    for j in slovar:
        if slovar[j][1] % 2 == 0:
            print(slovar[j])
        else:
            print()

else:
    print('')

