# A = [0] * int(input())
# for i in range(len(A)):
#     A[i] = int(input())
# print(A)        

a = int(input())
b = int(input())

A = []
for i in range (2,a+1):
    if a % i == 0:
        A.append(i)  
B = []
for i in range (2,b+1):
    if b % i == 0:
        B.append(i)  #в списках сейчас делители чисел

C = A + B
C.sort(reverse = True)
print(C)

def d(C):
    for i in C:
        if C.count(i) >= 2:      
            return i
    return 1
print(d(C))

def equation(x,y, max = 100):
    solutions = []
    for x in range(1,max+1):
        for y in range(1,max+1):
            if a*x+b*y == d(C):
                solutions.append(x)
                solutions.append(y)
    return solutions
print(solution) 




        

#print(A,B, sep = ' ')
