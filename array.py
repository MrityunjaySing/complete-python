# creating  array by importing arry
import array as arr
a = arr.array('i', [1, 2, 3])
print("the new created array is:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
    print()
# creating in array float type
b = arr.array('d',[2.5, 3.5, 4.5])
# print original array
print("the new array is:", end=" ")
for i in range (0, 3):
 print(b[i], end=" ")