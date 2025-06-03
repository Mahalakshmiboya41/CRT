'''
# Single inheritance:
What ever the class we want inherit write that in the brackets

'''
#single
class father():
    def father_method():
        return "This is father method"
# inheriting father class
class child(father):
    def child_method():
        return "This is child method"
parent_object=father # it has the properties of father
child_object=child   # it has properties of both
print(parent_object.father_method())
print(child_object.child_method())
print(child_object.father_method())