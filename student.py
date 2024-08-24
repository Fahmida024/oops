class Student():
    name=''
    age='12'
    grade='8'
    teacher='Meher'
    def __init__(self):
        print('Making a new instance')
    def changedetails(self):
        self.name=input('What is the name?')
    def showdetails(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.teacher)



student1=Student()
student1.changedetails()
student1.showdetails()
student2=Student()
student2.changedetails()
student2.showdetails()