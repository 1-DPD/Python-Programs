num = ""
number = [i for i in input("Enter a number : ")]
number.sort()
number.reverse()
for i in number:
    num += i
print(num)
