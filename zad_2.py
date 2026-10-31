from datetime import date
from zad_1 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Informacje dotyczące biblioteki:\n"
                f"Miasto: {self.city}\n"
                f"Ulica: {self.street}\n"
                f"Kod pocztowy: {self.zip_code}\n"
                f"Godziny otwarcia: {self.open_hours}\n"
                f"Numer telefonu: {self.phone}\n")


class Employee:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            hire_date: date,
            birth_date: date,
            city: str,
            street: str,
            zip_code: str,
            phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Dane pracownika:\n"
                f"Imię: {self.first_name}\n"
                f"Nazwisko: {self.last_name}\n"
                f"Data urdzoenia: {self.birth_date}\n"
                f"Zamieszkałe miasto: {self.city}\n"
                f"Ulica: {self.street}\n"
                f"Kod pocztowy: {self.street}\n"
                f"Numer telefonu: {self.phone}\n")


class Book:
    def __init__(
            self,
            library: Library,
            publication_date: date,
            author_name: str,
            author_surname: str,
            number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Dane dotyczące książki:\n"
                f"Biblioteka: {self.library}\n"
                f"Imię autora: {self.author_name}\n"
                f"Nazwisko autora: {self.author_surname}\n"
                f"Liczba stron: {self.number_of_pages}\n")


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


lib1 = Library("Czeladź", "Reymonta", "41-250",
               "7.00 - 8.00", "+48 213 742 241")
lib2 = Library("Katowice", "1 Maja", "40-001",
               "7.00 - 8.00", "+48 213 202 241")

b1 = Book(lib1, date(1993, 1, 1), "Andrzej", "Sapkowski", 332)
b2 = Book(lib1, date(1961, 6, 1), "Stanisław", "Lem", 204)
b3 = Book(lib2, date(1834, 6, 28), "Adam", "Mickiewicz", 340)
b4 = Book(lib2, date(1884, 3, 2), "Henryk", "Sienkiewicz", 610)
b5 = Book(lib1, date(1949, 6, 8), "George", "Orwell", 328)

e1 = Employee("Anna", "Kowalska", date(2015, 3, 1),
              date(1985, 7, 12), "Czeladź", "Szkolna 5", "41-250",
              "+48 501 234 567")
e2 = Employee("Piotr", "Nowak", date(2019, 9, 16),
              date(1992, 11, 3), "Katowice", "Mariacka 10", "40-014",
              "+48 602 345 678")
e3 = Employee("Marta", "Wiśniewska", date(2022, 1, 10),
              date(1998, 2, 25), "Sosnowiec", "Warszawska 3",
              "41-200", "+48 703 456 789")

s1 = Student("Kasia", [80, 75, 90, 60])
s2 = Student("Tomek", [40, 55, 30, 45])
s3 = Student("Ola", [65, 70, 50, 85])

o1 = Order(e1, s1, [b1, b2, b5], date(2026, 10, 20))
o2 = Order(e2, s3, [b3, b4], date(2026, 10, 24))

print(o1)
print(o2)
