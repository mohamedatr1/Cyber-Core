class Movies():
    def __init__ (self, titlle, director, year, genre):
        self.title = titlle
        self.director = director
        self.year = year
        self.genre = genre
    def display_movie(self):
        print("\n")
        print(f"The Title : {self.title}")
        print(f"The director : {self.director}")
        print(f"Release year : {self.year}")
        print(f"The Genre : {self.genre}")
        print("\n")
    

    def change_director(self, new_director):
        self.director = new_director



movie1 = Movies("Inception", "Christopher Nolan", "2010", "Sci_FI")
movie2 = Movies("The godfather", "Francis Ford Coppola", "1972", "Crime")
movie3 = Movies("Parasite", "Bong Joon-Ho", "2019", "thriller")

print("____ Movies _____")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()
print("Changing the director....")
movie1.change_director("khalil")
movie2.change_director("Abdou")
movie3.change_director("Bachir")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()


