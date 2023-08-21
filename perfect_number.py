def proper_divisor(n):
	divosor_list=[]
	for i in range(1,n+1):
		if i < n and n%i==0:
			divosor_list.append(i)
	return divosor_list	 


#number =int(input("En:ter a number."))
for number in range(1,10000):
	sum_list= proper_divisor(number)
	sum =0
	for i in sum_list:
		sum += i
	#print(sum_list, sum)
	if sum == number:
		print(f"YES! {sum} is a Perfect Number")
	#else :
		#print("It's NOT a perfect Number.")