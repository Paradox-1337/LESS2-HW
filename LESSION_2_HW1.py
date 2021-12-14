# 1. Выяснить тип результата выражений:
#
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
a, b, c, d = 15 * 3, 15 / 3, 15 // 2, 15 ** 2
list_test = [a, b, c, d]

for el in list_test:
    print(type(el))
