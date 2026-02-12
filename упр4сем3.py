
n = int(input())
A = ['c']*n
#A[0] = 'c'
#A[1] = 'cc' 
for i in range(n//2 + 1):
    A[i] = 'c'*(i+1)
     
for j in range(n//2 + 1, n):
    A[j] = A[j-1][:-1]   #следить за тем чтобы j попадало в ренжу
if n % 2 == 0:
    A.append('c')
print(A)
print('\n'.join(A))





 
    