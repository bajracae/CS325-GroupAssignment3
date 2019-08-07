import time
import random

print("Method 1 times")

n = 100 #size of first A

for i in range(0, 9): #controls size of N for 100 to 1000
    meanA = [] # holds the means of each size N. sum and divide later
    for j in range(0, 10): # runs through 10 times
        A = []

        for k in range(0, n): #generates array of size n with random ints
            A.append(random.randint(1, 100))

        count = 0 # count for swaps
        t1 = time.time() #set time before algo
        for p in range(0, n - 1):
            for q in range(p+1, n):
                if(A[p]>A[q]):
                    count+=1
        t2 = time.time() # set time after algo
        meanA.append(t2 - t1) # store time to run in meanA
    sum = 0
    for j in range(0, 10):
        sum += meanA[j]
    print("n = ", n, "time = ", sum/10)

    n+=100


A = [] #array containing variables to be sorted
n = 1000 #size of first A

for i in range(0, 9): #controls size of N for 100 to 1000
    meanA = [] # holds the means of each size N. sum and divide later
    for j in range(0, 1): # runs through 10 times
        A = []

        for k in range(0, n): #generates array of size n with random ints
            A.append(random.randint(1, 100))

        count = 0 # count for swaps
        t1 = time.time() #set time before algo
        for p in range(0, n - 1):
            for q in range(p+1, n):
                if(A[p]>A[q]):
                    count+=1
        t2 = time.time() # set time after algo
        meanA.append(t2 - t1) # store time to run in meanA
    #sum = 0
    #for j in range(0, 10):
    #    sum += meanA[j]
    print("n = ", n, "time = ", t2 - t1)
    n+=1000






#count = 0

#for i in range(0, n - 1):
#    for j in range(i+1, n):
#       if(A[i]>A[j]):
#           count+=1
#print(count)