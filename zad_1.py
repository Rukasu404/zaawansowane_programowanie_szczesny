class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Imie studenta: {self.name}"

    def is_passed(self) -> bool:
        grade_average = sum(self.marks) / len(self.marks)
        return grade_average > 50

s1 = Student("Łukasz", [70, 60, 20, 80, 60, 65, 40, 50])
s2 = Student("Jacuś", [30, 30, 30, 20, 30, 30, 30])

if __name__ == "__main__": #dodany warunek żeby ta część nie przeszkadzała po imporcie klasy do kolejnego zadania
    print(s1.is_passed())
    print(s2.is_passed())
