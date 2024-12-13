from random import randint
from datetime import datetime
"""
Задача о рюкзаке...
Данный способ не претендует на точность решения.
Подробное описание добавлю позже...
"""
#
d1 = datetime.now()
# Сгенерируем список условных "слитков"
# Вес "слитков" и емкость рюкзака в условных "попугаях"
list_of_p = []
for index in range(1_000_000):
    """  float( "x" + "." + "xxx" )  -->  1.234  """
    list_of_p.append(float(str(randint(0, 9)) + '.' + str(randint(0, 999))))
#
d2 = datetime.now()
# Тестовые данные для емкости рюкзака bp = all * 0.7
# list_of_p = [3.4, 5.69, 6.78]
# list_of_p = [2.22, 3.24, 5.64]
# list_of_p = [0.82, 3.19, 7.9]

print("LEN: ", len(list_of_p))
list_of_p = sorted(list_of_p, reverse=True)
# print(f'Найдено: {list_of_p}')
all = sum(list_of_p)
print(f'Сумма найденного: \t{all}')
bp = all * 0.7  # parrots
print(f'Ёмкость рюкзака: \t{bp}')

"""
Наполним рюкзак
"""
rz_list = []
for item in list_of_p:
    if bp >= item:
        rz_list.append(item)
        break
    else:
        """
        Если большой "слиток" не влез в рюкзак, отбросим и те что больше него
        цель: найти срез 98_|7|654321
        """
        continue

# print(rz_list)
ost_list = list.copy(list_of_p[(list_of_p.index(rz_list[0]) + 1):])
# print(ost_list)
sum_rz = sum(rz_list)
#
d3 = datetime.now()
#
for item in ost_list:
    free_space = bp - sum_rz
    if free_space >= item:
        rz_list.append(item)
        sum_rz += item
#
d4 = datetime.now()
#
result = sum_rz
print(f'\n\tРюкзак:\t\t\t{bp}\n\tПоместилось:\t{result}\n')
# print(f'\n\tСписок:\t\t\t{rz_list}')
dt_all = [d1, d2, d3, d4]
for index in range(len(dt_all) - 1):
    print(f'{index + 1}-{index + 2}: {dt_all[index + 1] - dt_all[index]}')
print(f'\n.................................................')
