class grandfather():
    def grandfather_method():
        return "This is grandfather class"
class father(grandfather):
    def father_method():
        return "This is father class"
class child(father): # Two classes should be inherrited, this is the syntax for inheritance
    def child_method():
        return "I have properties of grandfather and father"
grandfather_obj=grandfather
father_obj=father
child_obj=child
print(grandfather_obj.grandfather_method())
print(father_obj.father_method())
print(father_obj.grandfather_method())
print(child_obj.child_method())
print(child_obj.father_method())
print(child_obj.grandfather_method())