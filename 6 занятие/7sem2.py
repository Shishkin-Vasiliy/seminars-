a = list(input().split())
dict = {}
for i in range(len(a)):
    dict[i] = a.count(a[i])
C = (max(dict.values()))   
for j in range(len(a)):
    if a.count(a[j]) == C:
        print(a[j])
        break

