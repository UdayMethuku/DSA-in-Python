from collections import Counter
a=input("enter string:")
b=input("enter string:")
if len(a) != len(b):
    print("not anagram")
else:
    if Counter(a) == Counter(b):
        print("YES! it is anagram")
    else:
        print("not anagramliste")

# second method to check anagram
   # a=input("enter string:")
   # b=input("enter string:")
   
   # if sorted(a) == sorted(b):
   #     print("YES! it is anagram")
   # else:
   #     print("not anagram")

