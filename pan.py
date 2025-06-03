str=input("enter the pan number:")
if len(str)!=10:
    print("False")
if ((str[-1].isalpha()) and (str[0:5].isalpha()) and (str[5:9].isdigit()) and str.isupper()):
    print("True")
else:
    print("False")
