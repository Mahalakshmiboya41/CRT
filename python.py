a=10000
while(a!=0):
    b=input("enter (deposit/wd/available/exit): ")
    if(b=="deposit"):
      c=int(input("enter the deposit amount: "))
      a+=c
      print("deposit:",c)
      print("available:",a)
    elif(b=="wd"):
      d=int(input("enter the wd amount: "))
      d>a
      print("Insufficent balancce")
    elif(b=="wd"):
      d=int(input("enter the wd amount: "))
      a-=d
      print("wd:",d)
      print("available:",a)
    elif(b=="available"):
       print("available")
    elif(b=="exit"):
       print("exit")