class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
    
    def avg_grade(self):
        if self.grades:
            avg = sum(self.grades) / len(self.grades)
            return avg
        else:
            return 0

s1 = Student("Apeksha", 19, [98, 92, 95])
s2 = Student("Sharvari", 19, [88, 92, 85])
s3 = Student("Priya", 19, [89, 94, 88])
s4 = Student("Sneha ", 19, [90, 92, 90])

s1.display_details()
print(f"Average Grade: {s1.avg_grade()}\n")

s2.display_details()
print(f"Average Grade: {s2.avg_grade()}\n")

s3.display_details()
print(f"Average Grade: {s3.avg_grade()}\n")

s4.display_details()
print(f"Average Grade: {s4.avg_grade()}\n")
