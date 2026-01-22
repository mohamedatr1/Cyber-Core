class Messenger :
    def __init__(self, name_morsil, name_mosta9bil, message, date):
        self.name_morsil = name_morsil
        self.name_mosta9bil = name_mosta9bil
        self.message = message
        self.date = date


first_message = Messenger("Mohamed", "Abdou", "Win rak!!", "1:46")
second_message = Messenger("Abdou", "Mohamed", "Rani f dar", "1:47")

print(f"""
{first_message.name_morsil} Sent : ( {first_message.message} ) to : {first_message.name_mosta9bil} at : {first_message.date}

{second_message.name_morsil} Sent : ( {second_message.message} ) to : {second_message.name_mosta9bil} at : {second_message.date}
""")