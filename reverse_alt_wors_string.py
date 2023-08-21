rev_str = " "
str1 = []
user_input = [x for x in input("Enter a string : ").split(" ")]
print(f"Given string is :{user_input} ")

for i in range(len(user_input)):
    if i % 2 == 0:
        str1.append("".join(list(reversed(user_input[i]))))
    else:
        str1.append(user_input[i])
for s in str1:
    rev_str = rev_str + s + " "
print(f"Reverse of a given string is : {rev_str} ")
