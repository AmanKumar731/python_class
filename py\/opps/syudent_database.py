class Student:

    def __init__(self,name,grade,admiNum):
        self.name=name
        self.grade=grade
        self.admiNum=admiNum


    def is_passing(self):
        return self.grade>=60
    
    def details(self):
        return f"{self.name} (admission Number :{self.admiNum}) has a grade of {self.grade}"
    

student1 = Student("aman", 0, 2345)

print(student1.details)