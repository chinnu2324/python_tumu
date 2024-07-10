x = 'Dive into theory and complete enumerous practices exercises to master your coding skills.'
list=x.split(" ")
wordlen = 1
longestword=[]
for y in list:
    length = len(y)
    if length > wordlen:
        wordlen = length
        longestword=[y]
    elif(length == wordlen):
        longestword.append(y)
print("Longest Word is :", longestword)
    
