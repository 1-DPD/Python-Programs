T = int(input())
for  n in range(T):
    li1=[1]
    li2=[2]
    X=int(input())
    for s in range(X):
        li1.append(li1[s]+3)
        li2.append(li2[s]+3)
    if X==0 or X%3==0:
        print("NORMAL")
    elif X in li1:
        print("HUGE")
    elif X in li2:
        print("SMALL")