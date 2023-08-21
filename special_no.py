def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)


def special(special_no):		
#special_no = input("Enter a number.")
	number_list = [int(x) for x in special_no]
	#print(number_list)
	factorial_list = []
	for i in number_list:
		fact = factorial(i)
		factorial_list.append(fact)
	#print(factorial_list)
	sum=0
	for i in factorial_list:
		sum += i
	#print(sum)
	if sum == int(special_no):
		print("Special Numbers from 1 to 1000 are : ")
		print(sum)
		#print("Given Number is a Special Number .")
	#else:
	#	print("Given Number is NOT a Special Number")
for i in range(1,100000):
	special(str(i))