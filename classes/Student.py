class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Imie studenta: {self.name}"

    def is_passed(self) -> bool:
        grade_average = sum(self.marks) / len(self.marks)
        return grade_average > 50
