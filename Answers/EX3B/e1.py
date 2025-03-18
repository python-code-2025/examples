class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    
    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}")