import os 
import time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

 
class Gym:
    def __init__(self, first_name, last_name, id , status= "inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status

    def display_info(self):
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Member Id : {self.id}")
        print(f"Member Status : {self.status}")
        print("_" * 20)
    def status_active(self, new_status):
        self.status = new_status

members = []

def user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    id = input("Enter membership Id: ")
    status = input("Enter membership status , or click enter: ")
    if not status:
        status = "inactive"
    return Gym(first_name, last_name, id, status)
#بداية فانكشن البحث
def search_member(members):
    clear_screen()
    search = input("""
Search by:
1. Membership Id
2. First name
3. Membership Status                       

Enter your choice...
""")
    found_members = []
    if search == "1" :
            search_id = input("Enter the membership id to search:")
            for x in members :
                if x.id == search_id :
                    found_members.append(x)
                    break
    elif search == "2":
        search_name = input("Enter the first name to search:")
        for x in members:
            if x.first_name.lower() == search_name.lower() :
                found_members.append(x)
    elif search == "3":
        search_status = input("Enter the Status to search (active / inactive):")
        for x in members:
            if x.status.lower() == search_status.lower():
                found_members.append(x)
    else:
        print("Invalid choice! Try again...")

    if found_members :
        clear_screen()
        print("Members found:")
        for x in found_members:
            x.display_info()
    else:
        print("Member not found!")
    time.sleep(2)

#نهاية فانكشن البحث
while True :
    print("Welcom to Gym membership Management")
    entered = input("""
Choose an action :
1. Add new Memeber
2. Display all Members
3. Search for a member 
4. Exit                     
""")
    if entered == "1":
        members.append(user_info())
        print("User added succesfully")
        time.sleep(2)
    elif entered == "2":
        clear_screen()
        print("Displaying Users....")
        time.sleep(1)
        if len(members) > 0:
            for member in members :
                member.display_info()
                time.sleep(1)
            input("Press enter to return ....")
        else:
            print("No member to display ... ")
        
    elif entered == "3":
        if members :
            search_member(members)
        else:
            print("no members to search!")
            time.sleep(2)
    elif entered == "4":
        print("Exiting ....")
        break
    else :
        print("Invalid choice! Try again..")

 



