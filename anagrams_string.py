def anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return "Anagram"
    else:
        return "Not Anagram"


str1 = input("Enter First String : ").upper()
str2 = input("Enter second string : ").upper()
print(anagram(str1, str2))
