'''
POLYMORPHISM
'''
class Animal():
    def speak():
        return "Animal is speaking"
class bird():  #If we use inheritance here then method overridding arises bird(Animal)
    def speak():
        return "Bird is speaking"
animal_obj=Animal
bird_obj=bird
print(animal_obj.speak())
print(bird_obj.speak())