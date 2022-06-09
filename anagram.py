string1=input("Enter the String : ");
string2=input("Enter the String2 : ");
s1=string1.lower();
s2=string2.lower();
if(sorted(s1)==sorted(s2)):
    print("Given Strings are  anagrams");
else:
    print("Given Strings are not anagrams");