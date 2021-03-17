# Demo program to define and use a Class

# class student:
#     """ Class Developed By Arjun As A Demo"""
#     def __init__(self):
#         self.name = 'Arjun'
#         self.rollno = 18
#         self.marks = 95
#
#     def talk(self):
#         print('Hello I am:', self.name)
#         print('My Roll No is:', self.rollno)
#         print('My Marks are:', self.marks)
#
# s = student()
# print(s.name)
# print(s.rollno)
# print(s.marks)
# s.talk()

# Another Method

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print ( 'Hello I am:', self.name )
        print('My Roll No is:', self.rollno)
        print('My Marks are:', self.marks)

s1 = Student('Arjun', 18, 99)
s2 = Student('Keerthan', 19, 98)
s3 = Student('Asha', 20, 97)

s1.talk()
s2.talk()
s3.talk()
