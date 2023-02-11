#  Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

def give_array(q):
   arr = []
   for i in range(q):
      arr.append(int(input("Введите количество ягод на кусте: ")))
   return arr

n = int(input("Введите количество кустов (больше трех): "))
arr = give_array(n)
print(n-1)

max_sum = 0
for i in range(n):
   sum = 0
   if i == 0:
      sum = arr[i] + arr[i+1] + arr[n-1]
   if i > 1 and i < n-1:
      sum = arr[i] + arr[i+1] + arr[i-1]
   if i == n-1:
      sum = arr[i] + arr[i-1] + arr[0]

   if sum > max_sum:
      max_sum = sum
   sum = 0

print(max_sum)




