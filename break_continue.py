#Iteration Control Structures - 'break' & 'continue'
"""for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
 if(passenger=="FC" or passenger=="FA"):
  print("No check required")
 continue

 if(passenger=="SP"):
    print("Declare emergency in the airport")
 break
if(passenger=="A" or passenger=="C"):
 print("Proceed with normal security check")
print("Check the person")
print("Check for cabin baggage")

#infinite loop
 counter = 5
while (counter >= 5):
    print(counter)
    counter = counter + 1

num_list = [1,2]
for num in num_list:
    print(num, end = " ")"""

# print break statement

print("Using on the break statement")
for br in range(1,10):
    if br==3 :
     break
     print("Inside loop: ", br)
print("this is outside loop")

# continue keyword using
for i in range(1, 10):
    if i == 3:
     continue
    print("Inside loop: ", i)
print("this is outside loop")
