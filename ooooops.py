class Library:
    def __init__(self, acc_number, publisher, title, author):
        self.acc_number = acc_number
        self.publisher = publisher
        self.title = title
        self.author = author

    def read(self):
        self.acc_number = input("Enter accession number: ")
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")

    def compute(self, days_late):
        fine = days_late * 1.50
        print("Fine charged: $", fine)

    def display(self):
        print("Accession Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)


# Example usage:
library_book = Library("", "", "", "")  # Creating an instance of the Library class

# Reading data
library_book.read()

# Displaying data
print("\nBook Information:")
library_book.display()

# Computing fine
days_late = int(input("Enter number of days late: "))
library_book.compute(days_late)
