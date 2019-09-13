################

# Author: Zane Dawson

# Date: 09/11/2019

# This program finds and prits all prime numbers

# from 1 to 100.

################ 

#variable initialzation
arr = [] #array for prime numbers
count = 0 #count of multiples found

#loops through all integers from 1 to 100
for i in range(1, 101):
    #loops through all numbers less than the current i value
    for j in range(1, i):
        #checks if the j value is a multiple
        if(i % float(j) == 0):
            #counts the multiples of i
            count += 1
    #if the i value is a prime then the count will only be 1
    if(count == 1):
        #adds the i value to the array of prime values
        arr.append(i)
    #resets the count
    count = 0
#prints the array
print(arr)
