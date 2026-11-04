from datetime import date
from classes.Book import Book
from classes.Employee import Employee
from classes.Student import Student


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list[Book], order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_text = ""
        for book in self.books:
            books_text += str(book) + "\n"

        return (f"Informacje dotyczące zamówienia:\n"
                f"Pracownik obsługujący: {self.employee}\n"
                f"Student: {self.student}\n"
                f"Książki:\n{books_text}"
                f"Data złożenia zamówienia: {self.order_date}\n")
