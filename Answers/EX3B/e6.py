class Movie:
    def __init__(self, title, director, year):
        self.__title = title
        self.__director = director
        self.__year = year
    
    @classmethod
    def from_string(cls, movie_str):
        __title, __director, __year = movie_str.split(", ")
        return cls(__title, __director, int(__year))
    
    def getMovieInfo(self):
        print(f"Title:{self.__title}, Director:{self.__director}, Year:{self.__year}")

objectMovie1=Movie("Komisaario Palmun erehdys","Matti Kassila",1960)
objectMovie2=Movie.from_string("Kaasua komisaario Palmu, Matti Kassila, 1961")
objectMovie1.getMovieInfo()
objectMovie2.getMovieInfo()