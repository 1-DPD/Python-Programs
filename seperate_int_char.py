def digit_char(expression):
    digit = []
    alpha = []
    num = ''
    for c in expression:
        if c.isdigit():
            num += c
            print(num)
        else:
            if num:
                digit.append(int(num))
                print(digit)
                num += ""
            alpha.append(c)
    if num:
        digit.append(int(num))

    return digit, alpha


s = input("Enter String : ")
print(digit_char(s))
