import string 
def encrypt(message, shift):
    alphabets = string.ascii_lowercase
    encrypted_word = ""
    for letter in message :
        if letter.lower() in alphabets:
            original_position = alphabets.index(letter.lower())
            new_position = (original_position + shift) % 26
            encrypted_letter = alphabets[new_position]
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()   
            encrypted_word += encrypted_letter     
        else:
            encrypted_word += letter    
    print(encrypted_word)            
user_message = input("Enter a word: ")
user_shift = int(input("enter a shift: "))
encrypt(message=user_message ,shift=user_shift)    