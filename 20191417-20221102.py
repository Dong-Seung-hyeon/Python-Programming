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