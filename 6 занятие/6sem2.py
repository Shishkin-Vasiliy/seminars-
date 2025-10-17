numbers = list(input().split())
print(' '.join([numbers[i] for i in range(len(numbers)) if numbers.count(numbers[i]) == 1]))