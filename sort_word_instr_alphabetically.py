user_input = input("Enter a string (sentence) :  ")
str_list = [x for x in user_input.split(" ")]
str_list.sort()
str_index_list = []


def covert_listr(li):
    s = ""
    for i in li:
        s = s + i
    return s


main_op_str = ""
for i in range(len(str_list)):

    str_index = str_list.pop()
    # print(str_index)
    str_index_list = [i for i in str_index]
    str_index_list.sort()
    # print(str_index_list)
    final_str = covert_listr(str_index_list)
    main_op_str = final_str + " " + main_op_str


print(main_op_str)
# print(str_list)
