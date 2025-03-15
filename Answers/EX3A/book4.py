class Book:
    def __init__(self,title, author):
        self.__title=title
        self.__author=author

    def get_details(self):
        print(f"The title is {self.__title} and the author is {self.__author}")