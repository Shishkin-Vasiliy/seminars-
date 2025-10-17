raw = input()
l = raw.split() #чтобы отделить число от строки
N, string = int(l[0]), l[1] #N = 3, string = 'ABC...'
#step = M/N где M - длина строки
M = len(string)
new = string[M//N -1::-1] #именно двоеточие
for i in range(0, M, M//N):
    new += string[i+M//N - 1:i - 1:-1] #срез в обратном порядке
    #string_list = string.split(sep='')
print(new)