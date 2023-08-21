max1=0
con=[]
cons=''

T=int(input())
for i in range(T):
    x=int(input())
    y=input()
    
    for s in y:
        if s in 'aeiou':
            if cons:
                con.append(cons)
                cons=''
        else:
            cons+=s
            if cons:
                con.append(cons)
    print(con)
    
	for n in con:
	    if len(n)>max1:
	        max1=len(n)
	        
	if max1>=4:
	    print('NO')
	else:
	    print('YES')