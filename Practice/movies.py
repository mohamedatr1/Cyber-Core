class Movies():
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre 
    def display_movie(self):
        print("\n")
        print(f"The title : {self.title}")
        print(f"The director : {self.director}")
        print(f"Release Year : {self.year}")
        print(f"Genre : {self.genre}")
        print("\n")
    def change_director(self, new_director):
        self.director = new_director
        
        

movie1 = Movies("Inception", "Christopher Nolan", "2010", "Sci_Fi")
movie2 = Movies("The Godfather", "Francis Ford Coppola", "1972", "Crime")
movie3 = Movies("Parasite", "Bong Joon-ho", "2019", "Thriller")        
print("____ Movies List ____")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()
print("Changing Movie Director...")
movie1.change_director("Jackie Chan")
movie2.change_director("Ahmed")
movie3.change_director("Mohamed")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()

