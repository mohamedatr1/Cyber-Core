class Recipe():
    def __init__(self, recipe, ingredients, time, instructions):
        self.recipe = recipe
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions
def food():
    recipe = input("Enter the recipe name: ")
    ingredients = input("Enter ingredients (comma-sepparated): ")
    time = input("Enter cooking time : ")
    instructions = input("Enter cooking instructions: ")
    return Recipe (recipe, ingredients, time, instructions)
food1 = food()
print(f"""
Displaying recipe ...
Name : {food1.recipe}
Ingredients : {food1.ingredients}
Cooking Time : {food1.time}
Instructions : {food1.instructions}
------------------
""")
