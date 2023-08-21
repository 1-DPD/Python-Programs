digit = []
final_exp = []
final_string = ""
exp = input("Enter a Expression : \n")
exp_list = [x for x in exp]
# print(exp_list)
for i in exp_list:
    if i.isdigit():
        digit.append(int(i))
        exp_list.remove(i)
# print(digit)
# print(exp_list)
for i in exp_list:
    for j in digit:
        if exp_list.index(i) == digit.index(j):
            new_exp = i * j
            final_exp.append(new_exp)
# print(final_exp)
for i in final_exp:
    final_string += i
print(final_string)