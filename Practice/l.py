import string
def encrypt(message, shift):
    alphabet = string.ascii_lowercase
    encrypted_message = ""
    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - shift) % 26
            encrypted_letter = alphabet[new_position]
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()
            encrypted_message +=  encrypted_letter
        else:
            encrypted_message += letter    
    print(f"Here is the original message: {encrypted_message}")      
user_message = input("Enter a word: ")
user_shift = int(input("enter a shift: "))
encrypt(message=user_message ,shift=user_shift)    

