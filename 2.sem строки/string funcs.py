S = input()
p = input()

def Z(S):
    n = len(S)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(i + z[i], r - i))
        while i + z[i] < n and S[z[i]] == S[i + z[i]]:
            z[i] += 1
            if i + z[i] > r:
                l = i
                r = i + z[i]          
    return z

res = Z(p + '#' + S)

def Pi(S):
    n = len(S)
    pi = [0 for _ in range(n)]
    for i in range(1, n):
        k = pi[i - 1]
        while S[i] != S[k] and k > 0:
            k = pi[k - 1]
        pi[i] = k     
        if S[i] == S[k]:
            pi[i] += 1
    return pi        

res1 = Pi(p + '#' + S)

print(len(p) in res)
print(len(p) in res1)
