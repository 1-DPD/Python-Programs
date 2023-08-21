li = []
for _ in range(int(input("Enter No of Elements In List.\n"))):
	char = input("Enter Elements in List\n").lower()
	li.append(char)
a = li.count('a')
e = li.count('e')
i = li.count('i')
o = li.count('o')
u = li.count('u')


print(li)
print(f"Number of 'a' : {a} \nNumber of 'e' : {e} \nNumber of 'i' : {i}\nNumber of 'o' : {o}\nNumber of 'u' : {u}")
