class Product :
    def __init__ (self, name, price, description, rate):
        self.name = name
        self.price = price
        self.description  = description
        self.rate = rate

first_product = Product("Parfum", 200 , "The best parfum in the world", 4.8)
second_product = Product("Savon", 150, "For sensitivy", 4.7)
third_product = Product("Airpods", 1200, "Listen to the best sound!!", 4.9)

print(f"""
The {first_product.name} is {first_product.description} and it is only with :{first_product.price} dinnar , his rate is : {first_product.rate}
This {second_product.name} is {second_product.description} and has a : {second_product.rate} rate and only with : {second_product.price} dinnar
{third_product.description} with {third_product.name} in only : {third_product.price} dinnar , and has a : {third_product.rate} rate
""")
