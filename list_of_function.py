""""mark_list=[78,90,90,95,83,95]

mark_pos=mark_list.index(90)
print("Index position of mark 90:", mark_pos)

mark_list.append(54)
print("After adding new marks:",mark_list)

mark_list.insert(2, 98)
print("After inserting 98 at the 2nd index position:",mark_list)

mark_list.pop(1)
print("After removing the marks at the 1st index position:",mark_list)

mark_list.remove(95)
print("After removing the first occurence of 95 from the list:",mark_list)"""

# question 1st
"""my_list=[0]*5
for index in range(1,5):
    my_list[index]=(index-1)*10
print(my_list)"""

# question 2
num_list = [1,33,31,5,26,7,8,92,10]
num = 7
flag = 0
for item in num_list:
    if(item == num):
        flag = 1
    else:
        continue
if(flag == 1):
    print(num, "found in the list")
else:
    print(num, "NOT found in the list")