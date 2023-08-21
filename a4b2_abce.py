def find_digit(expression):
    digit = []
    # alpha = []
    # num = ''

    exp_list = [x for x in expression]
    for i in exp_list:
        if i.isdigit():
            digit.append(int(i))
            exp_list.remove(i)

    return digit, exp_list


def find_alpha(num_list):
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']
    alpha_list = []
    for i in num_list:
        alpha_list.append(small[i])

    return alpha_list


op_str = ""
exp = input("Enter a expression : \n")
number, alpha = find_digit(exp)
print(alpha, number)


