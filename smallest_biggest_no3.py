num1, num2, num3 = map(int,input("Enter THREE Numbers for comparison ").split(" "))
if num1 > num2 and num1 > num3:
    print(f"Biggest No :{num1}")
    if num2 > num3:
        print(f"Smallest NO : {num3}")
    else:
        print(f"Smallest NO : {num2}")
elif num2 > num1 and num2 > num3:
    print(f"Biggest No :{num1}")
    if num1 > num3:
        print(f"Smallest NO : {num3}")
    else:
        print(f"Smallest NO : {num1}")
else:
    print(f"Biggest NO : {num3}")
    if num2 > num1:
        print(f"Smallest NO : {num1}")
    else:
        print(f"Smallest NO : {num2}")
