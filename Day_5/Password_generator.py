import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# if the number of letters the user wants is 4, so the range will be 1
# to 4 the (+1) is just to modify the range. to be range(1,5) which will be 1 to 4.
password_list = []
for char in range(1, nr_letters + 1):
    random_character=random.choice(letters)
    password_list  += random_character
for char in range(1, nr_symbols,1):
    random_character=random.choice(symbols)
    #print(random_character)
    password_list += random_character
for char in range(1, nr_numbers ,1):
    random_character=random.choice(numbers)
    #print(random_character)
    password_list += random_character
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")