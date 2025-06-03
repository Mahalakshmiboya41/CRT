class grandfather:
    def grandfather_method():
        return "This is grandfather class"
class father(grandfather): #This is inherited from the GF
    def father_method():
        return "This is father class"
class mother:
    def mother_method():
        return "This is mother class"
class child(father,mother): # Two classes should be inherrited, this is the syntax for inheritance
    def child_method():
        return "I have properties of mother and father"
grandfather_obj=grandfather
father_obj=father
mother_obj=mother
child_obj=child
print(child_obj.child_method())
print(child_obj.father_method())
print(child_obj.grandfather_method())
print(child_obj.mother_method())