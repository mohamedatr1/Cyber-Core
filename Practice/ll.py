class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title 
        self.description = description
        self.due_date = due_date
        self.status = status
    def display_task (self):
        print(f"The title : {self.title}")
        print(f"The description : {self.description}")
        print(f"The due date : {self.due_date}")
        print(f"The Status is  : {self.status}")
    def mark_as_complete(self):
        self.status = "complete"
            
        



task1 = Task("Review Syntax", "Review how to create a class and object", "2026-02-13", "incomplete")
task2 = Task(" Syntax", "Review how to ", "2026-12-13", "incomplete")
task1.display_task()
task1.mark_as_complete()
task1.display_task()

