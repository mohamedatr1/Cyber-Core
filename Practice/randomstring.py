import string 
sentence = input("Enter a sentence: ")
new_sentence = ""
for x in sentence :
    if x not in string.punctuation :
        new_sentence += x
print("***Her is the same sentence without punctuation : *** \n" + new_sentence)        
