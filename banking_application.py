class BankAccount():
   def __init__(self,name,balance):
      self.name=name
      self.balance=balance
      self.__balance=balance #Encapsulation
   def deposit(self,amount):
      if(amount>0):
         a=self.__balance+amount 
         return f"{a} is the amount after the deposited "
      else:
         return "Enter the valid amount"
   def wd(self,amount):
      if(amount<=self.__balance):
         self.__balance -=amount
         return f"{amount} is wd succesfully"
      else:
         return "Insufficent balance"
   def check_balance(self):
      return self.__balance
   def exit(self):
      return "Exit"


     