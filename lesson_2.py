# Lesson 2: Class
print("Lesson 2: Class")

# Ex1: A library contains 5 books. Create a program contain:
## a database of the books.
## a program to find the book info (functions: add more book into the database, find book follow its name)

print("Ex1: Library Management Program")

class Book:
    def __init__(self, name, author, year):
        self.name = name 
        self.author = author
        self.year = year
    def print_info(self, metadata=""):
        print(f"{metadata} This book is {self.name}, by {self.author}, written in {self.year}.")


class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []
    
    def add_book(self, book):
        self.book_list.append(book)

    def show_books(self):
    #    for i in range (len(self.book_list)):
    #         self.book_list[i].print_info()
            # print(f"{i+1}. {self.book_list[i].name}, {self.book_list[i].author}, {self.book_list[i].year}.")
        for i, book in enumerate(self.book_list):
            book.print_info(i + 1)

    def find_book(self, book_name):
        # new_book = str(input("Find a book: "))
        # self.book_list.find(new_book)
        for i in range(len(self.book_list)):
            if book_name == self.book_list[i].name:
                print(f"Yes! Found {book_name}.")
                return self.book_list[i]

# ---------------------------
book_1 = Book("Mat biec", "Nhat Anh", 2016)
book_2 = Book("Nhung ngoi sao xa xoi", "Le Minh Khue", 1971)
book_3 = Book("Chiec thuyen ngoai xa", "Nguyen Minh Chau", 1985)
book_4 = Book("Doan thuyen danh ca", "Huy Can", 1958)
book_5 = Book("Mua xuan nho nho", "Thanh Hai", 1980)

thuvienhanoi = Library("Thu Vien Ha Noi")
thuvienhanoi.add_book(book_1)
thuvienhanoi.add_book(book_2)
thuvienhanoi.add_book(book_3)
thuvienhanoi.add_book(book_4)
thuvienhanoi.add_book(book_5)

thuvienhanoi.show_books()
# output:
# 1: Mat biec
# 2: Nhung...
# ...


book_6 = thuvienhanoi.find_book("Mat biec")
book_6.print_info()
# thuvientrento = Library("Lib Trento")
# thuvientrento.add_book(book_6)