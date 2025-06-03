'''
ENCAPSULATION
>>>BINDING OF DATA
>>>MAKES THE DATA PRIVATE
>>>INCS SECURITY
IMP:getter & setters
'''
class Student:
    def __init__(self,marks):#default constructor
        self.marks=marks
        self.__marks=marks #private
    def getter(self):
        return self.__marks
    def setter(self,marks):
        self.__marks=marks
s1=Student(88)
# set the data:
s1.setter(89)
# get the data
ans=s1.getter()
print(ans)



