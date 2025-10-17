s = input()

palindrome = s[::-1] == s #true or false

mirror_dict = {'A':'A', 'H':'H', 'I':'I', 'M':'M', 'O':'O', 'T':'T','U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y','1':'1','8':'8', 'E':'3','3':'E','J':'L','L':'J','S':'2','2':'S','Z':'5','5':'Z'}

mirror_s = ''
for character in s:
    if character in mirror_dict:
        mirror_s += mirror_dict[character]
    else:
        #map придумать с мэпом более короткое решение
        #mirrored = False - это необязательно
        break    
mirrored = mirror_s[::-1] == s

if mirrored and palindrome:
    print(f'{s} is a mirrored palindrome.')  
elif mirrored:
    print(f'{s} is a mirrored string.')   
elif palindrome:
    print(f'{s} is a palindrome.')
else:
    print(s + 'is not a palindrome.')     







