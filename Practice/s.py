class Profile:
    def __init__(self, username, email, language):
        self.username = username
        self.email = email
        self.language = language
first_person = Profile("cr01.xr", "crisxr40@gmail.com", "English")
second_person = Profile("kh01.lil", "kh01xl@gmail.com", "Frensh")


print(f"""
The username of the first person is: {first_person.username}
The email is : {first_person.email}
the language is : {first_person.language}
The user name of the second person is : {second_person.username}
the email is : {second_person.email}
the laguage is : {second_person.language}
""")    
