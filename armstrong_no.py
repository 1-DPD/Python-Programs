def split_no(n):
	for i in n:
		digit = [int(x) for x in n]
	return digit

def power_find(given_list,length):
	power_list=[]
	for i in given_list:
		power_list.append(pow(i,length))
	return power_list

def find_sum(some_list):
	sum=0
	for i in some_list:
		sum+=i
	return sum


for i in range(1,100001):
	split_list = split_no(str(i))
	power = len(split_list)
	sum_list=power_find(split_list,power)

	#print(f"l={split_list} pow={power}")
	#print(power_find(split_list,power))
	addition=find_sum(sum_list)
	#print(find_sum(sum_list),addition)
	if i == addition:
		print(f"{i} is a Armstrong Number.")
