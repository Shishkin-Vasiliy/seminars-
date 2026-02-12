n = int(input())
def func(n):
    if n < 2:
        return []
    elements = []
    d = 2
    while n > 1:
        while n % d == 0:
            elements.append(d)
            n //= d
        d += 1       
    return elements
print(func(n)) 
degrees = [f"{func(n).count(num)}" for num in func(n)]
degrees1 = list(map(int, degrees))
print(degrees1)

output0 = [f"{func(n)[i]}^{degrees1[i]}" for i in range(len(degrees1))]
#print('*'.join(output))

output = []
for el in output0:
    if el not in output:
        output.append(el)
print(n,'=','*'.join(output))    
