n = int(input())
def func(n):
    if n < 2:
        return[]
    elements = []

    d = 2
  #  while n > 1: - -  это эквивалентно elements.append(n) в строчке 14

    while n % d == 0:
         elements.append(d)
         n //= d
    d += 1       
    elements.append(n)


    #for i in range(2,n+1):
        # if n%i == 0:
        #    for j in range (2,i+1):
        #        if i%j == 0:
        #            elements.append(j)
        #        elements.append(i)
            
         #   elements.append(i)
    primes = '*'.join(map(str, elements))
   
         

        
    return primes   
     
print(func(n))
         