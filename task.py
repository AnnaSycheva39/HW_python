# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#x = [2, 3, 5, 9, 3]
#print(x)
#summ = 0
#for i in range(1, len(x), 2):
    #if i % 2 == 1:
 #       summ += x[i]       
#print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def get_unic(my_list):
    unic = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            unic.append(my_list[i])
    return unic

print(get_unic(my_list))
