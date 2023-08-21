import random

digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*']


def convert_to_string(list_name):
    s = " "
    for i in list_name:
        s += i
    return s


num = int(input("How many numbers you want in your password ?\n"))
small_letter = int(input("How many small letter you want ?\n"))
cap_letter = int(input("How many capital letter ypu want ?\n"))
char_symbol = int(input("How many symbols you want ?\n"))
password_length = num + small_letter + cap_letter + char_symbol

password_list = []
for _ in range(num):
    selected_num = random.choice(digit)
    password_list.append(selected_num)
    #print(selected_num)
for _ in range(small_letter):
    selected_small = random.choice(small)
    #print(selected_small)
    password_list.append(selected_small)
for _ in range(cap_letter):
    selected_cap = random.choice(capital)
    #print(selected_cap)
    password_list.append(selected_cap)
for _ in range(char_symbol):
    selected_char = random.choice(symbol)
    #print(selected_char)
    password_list.append(selected_char)
print(password_list)
random.shuffle(password_list)
password_set = set(password_list)
print(password_set)
password = convert_to_string(password_list)
print(f"Here is your {password_length} character long password :{password}")
while password_length > len(password_set):
    for _ in range(password_length-int(len(password_set))):
        new_small=random.choice(small)
        password_set.add(new_small)
    password_new = convert_to_string(password_set)
    print("OPPS! Something went Wrong.\n")
    print("Processing......Please Wait a moment......")
    print(f"Here  is your New {password_length} character long password :{password_new}")