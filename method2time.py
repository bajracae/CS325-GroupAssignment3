import time
import random
            
# Python program for implementation of MergeSort 
def mergeSort(arr, n): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        n = mergeSort(L, n) # Sorting the first half and returns the current count
        n = mergeSort(R, n) # Sorting the second half and returns the current count
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i] 
                i+=1
            else: 
                n+=(len(L) - i) # If a swap is made, this will add the number of swaps made to current count
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L):
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return n #returns the current count
            
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
    
    
A = []
n = 100

for i in range(0, 9):
    meanA = []
    for j in range(0, 10):
        for k in range(0, n):
            A.append(random.randint(1, 100))

        count = 0 # count
        t1 = time.time() #set time before al
        mergeSort(A, count)
        t2 = time.time()
        meanA.append(t2 - t1)
    sum = 0
    for j in range(0, 10):
        sum += meanA[j]
    print("n = ", n, "time = ", sum/10)
        
    n += 100

A = []
n = 1000

for i in range(0, 9):
    meanA = []
    for j in range(0, 10):
        for k in range(0, n):
            A.append(random.randint(1, 100))

        count = 0 # count
        t1 = time.time() #set time before al
        mergeSort(A, count)
        t2 = time.time()
        meanA.append(t2 - t1)
    sum = 0
    for j in range(0, 10):
        sum += meanA[j]
    print("n = ", n, "time = ", sum/10)
        
    n += 1000
# printList(array)
# print(n)