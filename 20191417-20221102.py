# ex 7-1
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("홍길동")
student2 = Student("김철수")
print("학생1의 이름 = ", student1.name)
print("학생2의 이름 = ", student2.name)

print("학생1의 타입 = ", type(student1))
print("학생2의 이름 = ", type(student2))

# ex 7-2
class Student:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

student1 = Student("홍길동", "hong1234@email.com", "010-1234-5678")
student2 = Student("김철수", "kim1234@gmail.com", "010-3456-7890")
print("학생1의 이름 = ", student1.name)
print("학생1의 email = ", student1.email)
print("학생1의 phone = ", student1.phone)
print()
print("학생2의 이름 = ", student2.name)
print("학생2의 email = ", student2.email)
print("학생2의 phone = ", student2.phone)

# ex 7-3
class Student:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def to_print(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.email,
            self.phone
        )

students = [
    Student("홍길동", "hong1234@email.net", "010-1234-5678"),
    Student("김철수", "kim1234@gmail.com", "010-3456-7890"),
    Student("홍길동", "hong1234@email.net", "010-2345-6789"),
    Student("김철수", "kim1234@gmail.com", "010-4567-7890")
]
print("이름", "email", "phone", sep='\t\t')
print('-' * 50)

for student in students:
    print(student.to_print())

# ex 7-4
class PythonSchool:
    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone
    def printStud(self):
        print("이름: ", self.name)
        print("이메일: ", self.email)
        print("전화번호: ", self.phone)

student1 = PythonSchool("Hong kildong", "hong1234@email.com", "010-1234-5678")
student1.printStud()