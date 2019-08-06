array = [1, 9, 6, 4, 5]
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
    
n = 0 # count
n = mergeSort(array, n)
printList(array)
print(n)