# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
#
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

list_all = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
list_name = []
for el in range(len(list_all)):
    temporary_list = list_all[el].split(" ")
    hm_indexes = len(temporary_list) -1
    incorrect_name = temporary_list[hm_indexes]
    name = incorrect_name.lower().title()
    list_name.append(name)
    print("Привет,",name)


