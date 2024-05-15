
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

choosen_letters = ''
choosen_numbers = ''
choosen_symbols = ''
#gera letras eleatorias da lista com a função randint
for _ in range(int(nr_letters)):
    index_letter = random.randint(0, len(letters) - 1)
    random_letter = letters[index_letter]
    choosen_letters += random_letter

#gera numeros
for _ in range(int(nr_numbers)):
    index_number = random.randint(0, len(numbers) - 1)
    random_number = numbers[index_number]
    choosen_numbers += random_number
    #gera simbolos
for _ in range(int(nr_symbols)):
    index_symbols = random.randint(0, len(symbols) - 1)
    random_symbols = symbols[index_symbols]
    choosen_symbols += random_symbols

#a password final é colocada no randint e cada valor é sorteado
#correção a ser feita, cada elemento sorteado deve ser removido da lista
final_password = ''
passwords_str = choosen_numbers + choosen_letters + choosen_symbols

password_lists = []
for password_list in passwords_str:
    passwords_str = password_lists.append(password_list)

print(password_lists)

for password in password_lists:
    
    passwords_index = random.randint(0, len(password_lists) - 1)
    
    passwords = password_lists[passwords_index]
    final_password += passwords
    password_lists.pop(passwords_index)

print(password_lists)

for password in password_lists:
    
    passwords_index = random.randint(0, len(password_lists) - 1)
    
    passwords = password_lists[passwords_index]
    final_password += passwords
    password_lists.pop(passwords_index)
    
print(password_lists)
for password in password_lists:
    
    passwords_index = random.randint(0, len(password_lists) - 1)
    
    passwords = password_lists[passwords_index]
    final_password += passwords
    password_lists.pop(passwords_index)
print(final_password)

    

   