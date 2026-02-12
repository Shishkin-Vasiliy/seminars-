a = list(input().split())
L = len(a)
for i in range(0,L-1,2):
    a[i],a[i+1] = a[i+1],a[i]
print(' '.join(a))    
    

    



