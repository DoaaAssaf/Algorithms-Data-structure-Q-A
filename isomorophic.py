'''
we consider two strings are isomorphic when the chars in the first one repeat as the chars in
the second one
for example:
- doaa & ball are isomorphic because chars in the first one repeat as the chars in
the second one,  l in ball repeated twice as a in doaa with the same index
- sakora and felore are isomorphic for the same reason
-dede and dode are not isomorphic cause e repeated in index=1,3 while e in dode repeated once
 in index=3 and o repeated once too .

'''


s= "doaaaoasw"
t="siwwwoaa"

s1=""
s2=""
for i in s:
    s1 += str(s.index(i)) #index return the first index  of a char in the string

for i in t:
    s2 += str(t.index(i))

if s1 == s2 : #if the two indexes strings are equal
    print("isomorphic")
else:        #if the two indexes strings aren't equal
    print ("they aren't isomorphic")
