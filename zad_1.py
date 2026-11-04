from classes.Student import Student


s1 = Student("Łukasz", [70, 60, 20, 80, 60, 65, 40, 50])
s2 = Student("Jacuś", [30, 30, 30, 20, 30, 30, 30])

if __name__ == "__main__":  # added for the next task
    print(s1.is_passed())
    print(s2.is_passed())
