class classroom():
    def __init__(self, capacity, HR_teacher):
        self.capacity = capacity
        self.HR_teacher = HR_teacher
        self.students = []
    def add_students(self,firstname):
        if len(self.students) >= self.capacity:
            print(f"{firstname} cannot be added. already too many students")
        else:
            self.students.append(firstname)

    
room13l = classroom(9, "Ketty")

y13l = ["Harry","Angelo","Quin","Suki","Sammy","Praewa","Katy","Ariel","Andru","Angel"]

for student in y13l:
    room13l.add_students(student)

print(room13l.students)

