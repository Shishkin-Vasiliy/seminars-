mirror = {'E':'3', 'J':'L', 'M':'M', '5':'Z','2':'S', 'A':'A', 'B':'B','C':'C'}

P = input()
def palindrome_detector(P):
    if P == P[::-1]:
        return f'{P} is a palindrome'
    else:
        return f'{P} is not a palindrome'
    for i in range ((len(P)//2)+1,len(P)):
        if P[i] in mirror.keys:
            


    # if P != P[::-1]:
    #     if mirror.keys in P:
#print(palindrome_detector(P))              
             

    



