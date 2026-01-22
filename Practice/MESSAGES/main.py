RECIPTIONS_FILE = "Names/invited_names.txt"
TEMPLATE_FILE = "input/Letters/starting_letters.txt"


def read_templates():
    with open(TEMPLATE_FILE, "r") as file:
        return file.read()
    
def read_names():
    with open(RECIPTIONS_FILE, "r") as file:
        good_names = []
        for x in file.readlines():
            good_names.append(x.strip())
        return good_names
    
template = read_templates()
guests = read_names()


def generate_invitations():
    for guest_name in guests:
        new_letter = template.replace("{name}", guest_name).replace("{signature}", "[ATR]")
        output_file = f"Output/Ready_to_send/letter_for_{guest_name.lower()}.txt"
        with open(output_file, "w") as file:
            file.write(new_letter)
        print(f"Generated Invitation for {guest_name}")



generate_invitations()