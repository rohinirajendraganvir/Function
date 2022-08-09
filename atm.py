
# def atm():
#     print("welcome to atm...")
#     print("swipe your card...")
# pin=7890
# total_balance=0
# total=15000  
# pin=int(input("enter your pin..."))
# if pin==pin:
#         print("\ncheck balance,\ndeposit,\nwithdraw")
#         user=input("enter what you want...")
#         if user=="1"or user=="check balance":
#                 print(total)
#                 print("thanks for using atm")
#         elif user=="2"or user=="deposit":
#                 deposit=int(input("enter how much deposit you want..."))
#                 total_balance=(total+deposit)
#                 print("your deposit succesfully",total_balance)
#                 print("thanks for using atm")
#         elif user=="3"or user=="withdraw":
#                 withdraw=int(input("enter how much you want withdraw..."))
#                 if withdraw>total:
#                         print("your main balance is less")
#                         print("thanks for using atm")
#                 elif withdraw<total:
#                         total_balance=total-withdraw
#                         print("succesfully withdraw your balance",total_balance)
#                         print("thanks for using atm")
#                 else:
#                         print("your pin is incorrect")
# atm()






def my_function(x):
  return 5 * x

print(my_function(3))
my_function(5)
my_function(9)







































# print("atm programm\nwelcome to my atm\nswipe your card here")
# language=input("enter your language=")
# if language=="english":
#     print("choose your transaction\n1.balance enquary\n2.withdraw money\n3.deposit\n5.transfer_money\n6.quite")
#     transaction=input("enter your transaction=")
#     if transaction=="balance enquary":
#         swipe=input("do you want swipe your card=")
#         if swipe=="yes":
#             atm_pin=9140
#             pin=int(input("enter your pin="))
#             if pin==atm_pin:
#                 print("here you swipe your card,thanks for using")
#             else:
#                 print("wrong pin")
#         else:
#             print("thanks for using atm")
#     elif transaction=="withdraw money":
#         balance=10000
#         amount=int(input("enter your amount="))
#         total=balance-amount
#         if amount>0:
#             atm_pin=9140
#             pin=int(input("enter your pin="))
#             if pin==atm_pin:
#                 print(total,"is left")
#                 print("collect your cash")
#             else:
#                 print("wrong pin")
#         else:
#             print("enter a valid amount to proceed")
#     elif transaction=="deposit":
#         balance=10000
#         deposit=int(input("enter your deposit amount="))
#         total=balance+deposit
#         if deposit>0:
#             atm_pin=9140
#             pin=int(input("enter your pin="))
#             if pin==atm_pin:
#                 print(total,"is increase")
#                 print("your deposit is done successsfully and thanks for using atm")
#             else:
#                 print("wrong pin")
#         else:
#             print("enter a valid deposit amount")
#     elif transaction=="transfer_money":
#         balance=10000
#         transfer_money=int(input("enter your amout to transfer money="))
#         total=balance-transfer_money
#         if transfer_money>0:
#             atm_pin=9140
#             pin=int(input("enter your pin="))
#             if pin==atm_pin:
#                 print(total,"is left")
#                 print("your money has been transfered and thanks for using atm")
#             else:
#                 print("wrong pin")
#         else:
#             print("please enter a valid amount to proceed")
#     elif transaction=="quite":
#         quite=input("enter yes if you want to quite=")
#         if quite=="yes":
#             atm_pin=9140
#             pin=int(input("enter your pin"))
#             if pin==atm_pin:
#                 print("quite")
#             else:
#                 print("wrong pin")
#         else:
#             print("choose any transaction please")
#     else:
#         print("wrong pin,try again")
# else:
#     print("language is not found")