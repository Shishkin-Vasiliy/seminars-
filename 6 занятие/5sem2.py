a = list(input().split())
for i in range(len(a)):
     a.append(a[0])
     a.pop(0)
     break
print(a)



