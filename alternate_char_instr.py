def myfunc(input_string):
    output_string = ''
    for i, letter in enumerate(input_string):
        if i % 2 == 0:
            output_string += letter.lower()
        else:
            output_string += letter.upper()
    return output_string
str='defgshbkjb'
print(myfunc(str))
