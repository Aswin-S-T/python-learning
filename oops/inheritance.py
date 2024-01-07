class Person:
    def __init__(self,name,company,post):
        self.name = name
        self.company = company
        self.post = post

    def introduceMyself(self):
        print('My name is ',self.name)
        print('And iam working as a ', self.post)

class ModifiedPerson(Person):
    def __init__(self,name,company,post,yearOfExp):
        self.name = name
        self.company = company
        self.post = post
        self.yearOfExp = yearOfExp
        

    def introduceMyselfNew(self):
        print('Hey,')
        print("I'm ", self.name, " and I'm working as a ", self.post, " at ",self.company,". I have ", self.yearOfExp, " of experience.")

person1 = ModifiedPerson('Ashish','Qburst','Python developer', 3)
person1.introduceMyself()