# -*- coding: utf-8 -*-
"""Python Programming DAY 2 part 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uZfw4UWR-JtYtaCHUvWs6RQ3mbAc7AWB

Range
"""

for i in range(1,10,2):
  print(i)

myrange = range(8)

print(myrange)
print(list(myrange))

myrange = range(4,8)

print(myrange)
print(list(myrange))

myrange = range(2,20,3)

print(myrange)
print(list(myrange))

myrange = range(2,20,3)

for i in myrange:
    print(i)

list_1 = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11]
for i in range(0, len(list_1), 2):
  print(list_1[i])

step = int(input("Enter step value: "))

list_1 = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11]

for i in range(0, len(list_1), step):
  print(list_1[i])

step = int(input("Enter step value: "))

list_1 = [6, 4, 7, 2, 8, 3, 8, 3, 0, 6, 1]

for i in range(0, len(list_1), step):
  print(list_1[i])



