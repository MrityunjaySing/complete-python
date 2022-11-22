"""list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list5 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list5)
                    #type() which type of data
list1 = ["apple", "banana", "cherry"]
print(type(list1))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)"""

                  #Access Item indexing
"""list1 = ["apple", "banana", "cherry", "ram", "shyam", "arjun"]
print(list1[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist = [ "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print(" No 'apple' is in fruits list")

                 #change range item value
               #first type

list = ["satyam", "shivam", "ram", "shyam"]
list[1] = ["mrityunjay"]
print(list)
                        #secod type

list = ["satyam", "shivam", "ram", "shyam"]
list[1:2] = ["mrityunjay", "singh"]
print(list)
                      #third type

list = ["satyam", "shivam", "ram", "shyam"]
list.insert(2, "mrs")
print(list)

                       #fourth type using a extend() mathod

list = ["satyam", "shivam", "ram", "shyam"]
list2 = ["satyam", "shivam", "ramraj", "shyam"]
list.extend(list2)
print(list)
                  #To add an item to the end of the list use the append() method:

list = ["satyam", "shivam", "ram", "shyam"]
list.append(" mrityunjay ")
print(list)

                    # The remove() method removes the specified item.

list = ["satyam", "shivam", "ram", "shyam"]
list.remove("ram")
print(list)
                   # The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
                        #The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

                        #clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

                  #Loop Through the Index Numbers
                  #Use the range() and len() functions to create a suitable iterable.

thislist = ["satyam", "ram", "shyam"]
for i in range(len(thislist)):
    print(thislist[i])

                    #You can loop through the list items by using a while loop.
        #Use the len() function to determine the length of the list, then start at 0
    #  loop your way through the list items by refering to their indexes.

    thislist = ["satyam", "ram", "shyam"]
    i=0
while i < len(thislist):
        print(thislist[i])
        i=i+1 

        #List Comprehension offers the shortest syntax for looping through lists:
# on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["mango", "banana", "kiwi", "cherry", "apple"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)

             #With list comprehension you can do all that with only one line of code:

fruits = ["mango", "banana", "kiwi", "cherry", "apple"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]

 #You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)

       #Accept only numbers lower than 5:

newlist = [x for x in range(10) if x<5]
print(newlist)
#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)"""

 #List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
