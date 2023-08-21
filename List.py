print("**************************\n\nLet's Learn Something About List In Python\n\n****************************\n")
list_one=[1,4,5,6,3,4]
print(list_one)
print('This iS a original List ')

list_one.sort()
print(list_one)
print('This is sorting-.sort\n')

list_one.append(2)
print(list_one)
print('Adiing at last -.append()\n')

n=list_one.count(4)
print(n)
print('Will count occurence of number given -.count()\n')

list_one.pop()
print(list_one)
print('Will pop the last elemnt or can pop element at index -.pop()\n')

list_one.remove(4)
print(list_one)
print('will removwn them element given -.remove()\n')

i=list_one.index(4)
print(i)
print("will determine thr start index of a number/string-.insex()\n")

list_one.extend([5,6]) 
print(list_one)
print('will extend the list-.extend()\n')

lis_o=list_one.copy()
print(list_one)
print('will copy the list-.copy()\n')

list_one.clear()
print(list_one)
print('will clear a list-.clear()\n')

list_one.insert(0,8)
list_one.insert(1,3)
print(list_one)
print('insert the element at 2nd argument to the index of first argument-.insert()\n')
