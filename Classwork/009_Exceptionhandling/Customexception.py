# class AgeInvalidException(Exception):
#     pass

# def check_age(a):
#     if a>18:
#         print("Valid age")
#     else:
#         raise AgeInvalidException(f"Invalid age - wait for more {18-a} years")
        
# print("started")
# try :
#     check_age(10)
# except AgeInvalidException as e:
#     print(e)
# print("ended")

class InsuffecientBalanceException(Exception):
    pass

def balance(a):
    if a>1000:
        print(f"Your balance is {a}")
    else:
        raise InsuffecientBalanceException("Insufficient Balance for Withdrawl")

print("Start")
try:
    balance(500)
except InsuffecientBalanceException as e:
    print(e)
print("End")

# from abc import ABC,abstractmethod

# class BankAccountException(Exception):
#     pass

# class Account(ABC):
#     balance = 0
#     def check_balance(self):
#         print(f"Current balance is : {self.balance}")
    
#     @abstractmethod
#     def deposite(self,amount):
#         pass

#     @abstractmethod
#     def withdrow(self,amount):
#         pass

# class Saving(Account):

#     def deposite(self,amount):
#         self.balance += amount

#     def withdrow(self,amount):
#         if amount>self.balance:
#             raise BankAccountException("Insufficient balance")
#         else:
#             self.balance -= amount

# print("Start")
# try :
#     a1 = Saving()
#     a1.check_balance()
#     a1.deposite(3000)
#     a1.check_balance()
#     a1.withdrow(5000)
#     a1.check_balance()
# except BankAccountException as e:
#     print(e)
# # print("End")
