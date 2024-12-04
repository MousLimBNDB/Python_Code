import time ##just for the pauses
## The book class-----------------------------------------------------------------------------------------------

class Book():
    
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def get_discription(self):
            return f"{self.title} by {self.author}, published in {self.year}, {self.pages} pages.\n"
        
##how i debuted the program ,then i decided to turn it to an interactive "interface"--------------------------------
"""
library = []
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)
book2 = Book("1984", "George Orwell", 1949, 328)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813, 279)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180)
library = [book1,book2,book3,book4]

for book in library:
    print(book.get_discription())
    
def reseach(title):
    for book in library:
        if book.title.lower() == title.lower():
            return f"the book {title} is availble" 
    return f"the book {title} isn't availble"
        
print(reseach("1984"))
print(reseach("1985"))
"""

##the librery calss ------------------------------------------------------------------------------------------

class Librery ():
    def __init__(self):
        self.books =[]
        
    def add_a_book(self,title,author,year,pages):
        book_added = Book(title,author,year,pages)
        self.books.append(book_added)
        print(f"the book has been created")
        
    def reseach(self,title):
        for book in self.books:
            if book.title.lower() ==title.lower():
                             return f"the book {title} is availble" 
        return f"the book {title} isn't availble"
    
    
    def display_books(self):
        if not self.books:
            print("there is no books availble")
        else:
            print("Books availble in the library:\n")
            for book in self.books:
                print(book.get_discription())

## MAIN ----------------------------------------------------------------------------------------------------
                           
def main():
    librery = Librery()
    def input_integer(param, prompt):
        while True:
            user_input = input(prompt)
            try:
                value = int(user_input)
                if param == "year" and (0 < value <= 2024):
                    return value
                elif param == "pages" and value > 0:
                    return value
                else:
                    print("Please enter a valid input.")
            except ValueError:
                print("You entered an incorrect value. Please enter a number.")
    while True:
        print("\n welcom to our librery")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Display All Books")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input_integer("year","Enter publication year: ")
            pages = input_integer("pages","Enter number of pages: ")
            librery.add_a_book(title, author, year, pages)
            time.sleep(3)


        elif choice == '2':
            title = input("Enter book title to search: ")
            print(librery.reseach(title))
            time.sleep(3)


        elif choice == '3':
            librery.display_books()
            time.sleep(3)

        elif choice == '4':
            print("Exiting the librery ....")
            time.sleep(5)
            break

        else:
            print("Invalid choice. Please select a valid option.")
            
##--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()