add = 0
array = []
length = int(input("Enter length of a array : "))
# array = [int(n) for n in input("Enter a elements of array :")]
for n in  range(length):
    num = int(input("Enter a number in array : "))
    array.append(num)
for num in array:
    add += num
average = add / length
print(f"Average of numbers in user given array is : {average}")
