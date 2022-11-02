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