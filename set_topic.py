"""# Creating a set

set1 = set(["satyam", "For", "satyam"])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")

# Checking the element
# using in keyword
print("satyam" in set1)


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1

    #removing() method or discard() method
    #create set
    set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
    print("\n Initial set: ")
    print(set1)
    # this element set removing element remove()
    set1.remove(5)
    set1.remove(6)
    print("\n set after removeble two element: ")
    print(set1)

    # removing element form  set by discard() method:
    set1.discard(8)
    set1.discard(9)
    print("\n after removing using a discard method")

    # using iterator method
    for i in range(1,5):
        set1.remove(i)
        print("\n after removing ")
        print(set1)"""
print(" using a pop() method if remove only last element")

set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print("Initial set:")
print(set1)
 #using a pop() method uses
set1.pop()
print("\n after using a pop method:")
print(set1)
""""print("\n after clear to set using clear method")
set1.clrear()
print(set1)"""

# Python program to demonstrate that copy
# created using set copy is shallow
first = {'g', 'e', 'e', 'k', 's'}
second = first.copy()

# before adding
print('before adding: ')
print('first: ',first)
print('second: ', second)

# Adding element to second, first does not
# change.
second.add('f')

# after adding
print('after adding: ')
print('first: ', first)
print('second: ', second)

# Python program to demonstrate the
# use of update() method

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]

# Lists converted to sets
set1 = set(list2)
set2 = set(list1)

# Update method
set1.update(set2)

# Print the updated set
print(set1)

# List is passed as an parameter which
# gets automatically converted to a set
set1.update(list3)
print(set1)

number = {1, 2, 3, 4, 5}

num_Dict = {6: 'Six', 7: 'Seven', 8: 'Eight',9: 'Nine', 10: 'Ten'}

number.update(num_Dict)

print("Updated set: ", number)
