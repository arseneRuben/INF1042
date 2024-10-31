def inverse(ch):
    return ch[::-1]

def palindrome(ch):
    return ch == inverse(ch)

print('la chaine inversé est:',inverse('exemple'))
print('True or false, la chaine est un palindrome?:',palindrome('radar'))
print('True or false, la chaine est un palindrome?:',palindrome('bonjour'))


