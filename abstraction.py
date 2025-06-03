'''
>>>hiding un necessary info
>>>provides usefulinfo only
>>>abc module and abstractmethod
>>>@abstract
'''
from abc import ABC,abstractmethod #abc-module,ABC-class
class  four_wheeler(ABC):
    @abstractmethod
    def engine():
        pass #even if we write the return here it won't be exectuded

class swift(four_wheeler):#inheriting the properties of 4wheeler
    def car_start():
        return "car is moving"
car_1=swift
ans=car_1.car_start()
print(ans)
    
