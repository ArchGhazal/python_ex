vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
letter = input('Enter a letter')
for i in vowels:
    if i == letter:
        print(i , 'is a vowel')
        break 
else: print (i , 'is not a vowel')
