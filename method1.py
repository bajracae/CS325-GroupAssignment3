A = [2, 4, 1, 3, 5]
n = len(A)
count = 0

for i in range(0, n - 1):
    for j in range(i+1, n):
       if(A[i]>A[j]):
           count+=1
           print(A[i], " ", A[j])
print(count)