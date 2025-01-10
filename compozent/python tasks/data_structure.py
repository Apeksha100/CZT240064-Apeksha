students = {}

def add_s(student_id, name, age, grades):
    students[student_id] = {"name": name, "age": age, "grades": grades}

def view_s(student_id):
    return students.get(student_id, "Student not found.")

def update_s(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name: students[student_id]["name"] = name
        if age: students[student_id]["age"] = age
        if grades: students[student_id]["grades"] = grades
    else:
        return "Student not found."

def delete_s(student_id):
    if student_id in students:
        del students[student_id]
    else:
        return "Student not found."

add_s("1", "Apeksha", 19, [90, 94, 88])
add_s("2", "Sharvari", 19, [88, 92, 85])
add_s("3", "Sneha ", 19, [90, 94, 88])
add_s("4", "Priya", 19, [90, 94, 88])

print(view_s("1"))
update_s("1", grades=[99, 96, 98])
print(view_s("1"))
delete_s("2")
print(students)
