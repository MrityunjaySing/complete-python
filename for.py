 # FOR LOOP

print("Flight has landed")
print("Proceed for immigration check")
for passenger_count in 1,2,3,4,5:
    print("Immigration check done for passenger,", passenger_count)

       #for with range
start=1
end=10
step=2
for number in range (start, end, step):
 print("The current number is ", number)

                     #Iteration Control Structures - Nested Loops
number_of_passengers=7
number_of_baggage=3
security_check=True
for passenger_count in range(1, number_of_passengers+1):
 for baggage_count in range(1,number_of_baggage+1):
  if(security_check==True):
     print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
else:
 print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
