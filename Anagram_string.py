x = input("Enter your first string:").lower()
y = input("Enter your second string:").lower()
dict_count1 = {}
dict_count2={}
if(len(x)==len(y)):
    for i in x:
        if i in dict_count1:
            dict_count1[i] +=1
        else:
            dict_count1[i] =1
    for j in y:
        if j in dict_count2:
            dict_count2[j] +=1
        else:
            dict_count2[j] =1
    if dict_count1==dict_count2:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
else:
    print("Two string are not anagrams")
