n = int(input())
if n == 0:
    print('length is invalid')
    print('Минимальная стоимость: 0')
    print('Оптимальный путь: None')
    exit()
if n == 1:
    print('lenth is invalid') 
    print('Минимальная стоимость: 0')
    print('Оптимальный путь: None')  
    exit()
prices = list(map(int, input().split()))

dp = {}
dp[0] = [prices[0], -1]
dp[1] = [prices[0] + prices[1], 0]
 
   

for i in range(2, n):
    cost = min(dp[i - 1][0] + prices[i], dp[i - 2][0] + prices[i])
    if cost == dp[i - 1][0] + prices[i]:
        dp[i] = [cost, i - 1]
    else:
        dp[i] = [cost, i - 2]    
print(f'Минимальная стоимость:{dp[n - 1][0]}')
 
path = []
number = n - 1
while number >= 0:
    path.append(str(number))
    number = dp[number][1]
path.reverse() 

print(f'Оптимальный путь:{' '.join(path)}')