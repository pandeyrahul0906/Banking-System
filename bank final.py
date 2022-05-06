class user():
    usercount=0
    def __init__(self,first,last,gender,age):
        self.first=first.strip().title()
        self.last=last.strip().title()
        self.gender=gender.strip().title()
        self.age=age
        self.email=self.first+"."+last+"@itvedant.com"

class bank(user):
    def __init__ (self,first,last,gender,age):
        super().__init__(first,last,gender,age)
        self.__balance=0


    def viewbal(self):
        print(f" your account balance is {self.__balance}")


    def deposit(self,amt):
        self.__balance=self.__balance+amt
        print(f" your deposited amount is {amt}")


    def withdraw(self,amt):
        if(amt>=100 and self.__balance>amt):
            self.__balance=self.__balance-amt
            print(f" your account balance is {self.__balance}")
        else:
            print(f" you have insufficient balance")

    def transfer(self,user,amt):
        if(self.__balance>=amt and amt>0):
            self.__balance=self.__balance-amt
            user.__balance=user.__balance+amt
        else:
            print(f" you have insufficient balance")
if (__name__=="__main__"):
    a=bank("Rahul","Pandey","M","20")
    b=bank("Rohit","Yadav","F","20")
    while (True):
        print(f"Welcome  to the pandey's bank.\nEnter your choice")
        print("1. Viewbalance")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Transfer")
        print("Enter the number: ")
        user_choice=input()
        if user_choice not in["1","2","3","4"] 
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            a.viewbal()
            b.viewbal()

        elif user_choice==2:
            amt=input(int("enter the amount you want to deposite"))
            a.deposite(self,amt)
            b.deposite(self,amt)

        elif user_choice==3:
            amt=input(int("Enter the amount you want to withdram"))
            a.withdraw(self,amt)
            b.withdram(self,amt)

        elif user_choice==4:
            amt=input(int("Enter the amount you want to transfer"))
            a.transfer(self,user,amt)
            b.transfer(self,user,amt)

        else:
            print("Not a Valid Option") 
   
                














    
