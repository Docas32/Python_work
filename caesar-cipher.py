

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesa_cipher_logo import logo
print(logo)


def encrypt(text, shift):
    encripted = ''  
    for letter in text:
        if letter in alphabet:
              
            index = alphabet.index(letter) + shift % len(alphabet)
            encripted += alphabet[index]   
        else:
            encripted += letter
    print(f"The encoded text is {encripted}")
    
def decrypt(text, shift):
    decrypted = ''
    for letter in text:
        if letter in alphabet:
            index_letter = alphabet.index(letter) - shift % len(alphabet)
            decrypted += alphabet[index_letter]
        else:
            decrypted += letter
    print(f"The decoded text is {decrypted}")
        
condition = True
while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25   
    if direction == 'encode':    
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text,shift)
        
    botton = input("Type 'yes' if you want to continue or 'no' to exit " )
    if botton == 'yes':
        condition = True
    elif botton == 'no':
        condition = False
    else:
        condition = False