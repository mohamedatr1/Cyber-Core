book1 = input("Enter the name of a book you own: \n") 
book2 = input("Enter the name of another book you own (Or press 'Enter' to skip): \n") 
library = [book1 , book2] 

if book2 == "": 
    print(f"Your library : \n : {book1}") 
else : 
    print(f"Your Library : \n {library}" ) 

wish = input("Enter the name of a book you wish to have (Or press 'Enter' to skip) : \n") 
if wish == "": 
    print(f"Your Library : \n {library}" ) 
else : 
    another = input("Enter the name of another book you wish to have (Or press 'Enter' To Skip)") 
    wishlist = [ wish ,another] 
    if another == "": 
        print(f"Your wishlist : \n {wish}") 
    else : 
        print(f"Your wishlist : \n {wishlist} ") 

new = input("Enter the name of a book from your wishlist that you have acquired (Or press 'Enter' to skip):\n") 
if new == "": 
    print(f"Your Library : {library}") 
    print(f"Your Wishlist : {wishlist}") 
else : 
    library.append(new) 
    wishlist.remove(new) 
    print(f"""Your Library : {library} 
Your wishlist : {wishlist} """) 

donate = input("Enter the name of a book from your library you wish to donate (Or press 'Enter'to skip)") 
if donate : 
    if donate in library: 
        library.remove(donate) 
    else: 
        print("This book is not in your library!") 

print(f"Final Library : {library}") 

if new and new in wishlist: 
    wishlist.remove(new) 
    library.append(new) 
else : 
    library.append(new) 

print(f"""Your Library : {library} 
Your wishlist : {wishlist}""")
