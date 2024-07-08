# Algorithm for a palindrome

def ispalindrome(str):
    startindex = 0
    endindex = len(str) - 1
    
    for x in str:
        print(str[startindex])
        print(str[endindex])
        if str[startindex] != str[endindex]:
            return False
        startindex += 1 
        endindex -= 1    
    return True  
print(ispalindrome('bomb'))
#  second
x = input('Enter the word:')
y= x[::-1]
if x == y:
    print(f'{x} is a palindrome')
else:
    print(f'{x} is not a palindrome')
