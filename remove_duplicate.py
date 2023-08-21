li=[]
for i in range(int(input("Enter Number "))):
	char = input()
	li.append(char)
print(li)
new_list=[]
[new_list.append(x) for x in li if x not in new_list]
print(new_list)