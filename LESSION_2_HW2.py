# 2. Дан список:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
#
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
#
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
#
# Примечание: если обособление чисел кавычками не будет получаться -
# можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

list_start = ['в', 5, 'часов', 17, 'минут', 'температура', 'воздуха', 'была', -9, 'градусов']

list_end = []

for el in list_start:
    if isinstance(el, str):
        list_end.append(el)
    else:
        if el < 0 and el > -10:
            el = (f'{el:03}')
            list_end.append('"')
            list_end.append(el)
            list_end.append('"')
        elif len(str(el)) <= 1:
            el = (f'{el:02}')
            list_end.append('"')
            list_end.append(el)
            list_end.append('"')
        else:
            list_end.append('"')
            list_end.append(el)
            list_end.append('"')

print(" ".join(map(str, list_end)))
