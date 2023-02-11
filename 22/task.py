# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

def give_array(q):
   arr = []
   for i in range(q):
      arr.append(int(input("Введите элемент списка: ")))
   return arr


n = int(input("Введите количество элементов первого списка: "))
m = int(input("Введите количество элементов второго списка: "))
arr_one = give_array(n)
arr_two = give_array(m)

print(arr_one)
print(arr_two)

arr_end = []
for i in range(n):
   for j in range(m):
      if arr_one[i] == arr_two[j]:
         arr_end.append(arr_two[j])

print(arr_end)

arr_end = set(arr_end)
arr_end = list(arr_end)
print(arr_end)