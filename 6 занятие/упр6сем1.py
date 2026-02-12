f = open('text.txt')
a = f.readline()
numbers = list(map(str, a.split()))
print(numbers)
operation = f.readline()
base = f.readline()
print(operation,base)
numbers10 = []
#def filter(numbers): #фильтрация чисел
#   filternum = []
#   for num in numbers:
#     if all(z in '012345' for z in num):
#         filternum.append(num)
#   return filternum 
#numbers1 = filter(numbers)   
#print(numbers1)  
N1 = 0

for i in numbers:           
    print(len(str(i)))
    if len(str(i)) == 1:
        numbers10.append(int(i))
    else:
        for j in range(len(str(i)[::-1])):
         N1 += int(str(i)[::-1][j])*int(base)**j 
        numbers10.append(N1)
        N1 = 0
print(numbers10)
N2 = 0
if operation == '*\n':
   N2 = 1
for s in range(len(numbers10)):
   if operation == '+\n':
      N2 += numbers10[s] 
   elif operation == '-\n':
      N2 -= numbers10[s]
   elif operation == '*\n':
      N2 *= numbers10[s]
   print(N2)

M = []
while N2 // int(base) > 1:
   M.append(N2%int(base))
   N2 = N2 // int(base)

   if N2 <= 1:
      M.append(N2%int(base))
      break
print ((''.join(str(M[::-1])))) 
f.close()

f1 = open('output.txt', 'w')
for n in M:
   f1.write(str(n))
f1.close()           
      
               
