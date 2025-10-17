N = int(input())
numbers = list(map(int, input().split()))
#print(''.join(numbers))
A = 0
for i in range(len(numbers)):
    A += numbers[i] 
A //= N 
print(A)
dict = {}
for j in range(len(numbers)):
    if numbers[j] > A:
        dict[j] = numbers[j] - A
    else:
        dict[j] = A - numbers[j]   
print(dict)
print(min(dict.values()) + A)    



    