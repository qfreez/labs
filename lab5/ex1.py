class Book():
    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}.")

book = Book()
book.title = "The Art of Clean Code"
book.author = "Christian Mayer"
book.year = 2023
book.get_info()