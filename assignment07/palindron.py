string = input("enter your string:")
String = list(string) 
str2 = []
for s in range(len(String)//2):
    if String[s] == String[(s+1)*-1]:
        str2.append(s)
if len(str2) < len(String)//2:
    print(string, " is not palindrome", sep="")
else:
    print(string," is palindrome", sep="")