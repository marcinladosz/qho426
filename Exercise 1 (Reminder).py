#If the account type is "admin", display "Full access granted".
#If the account type is "employee", display "Limited access granted".
#If the account type is "guest", display "Guest access only".
#For any other input, display "Unknown account".#

acc_type = input("PLease enter the account type")
if acc_type == "admin":
    print("Full access granted")
elif acc_type == "employee":
    print("Limited access granted")
elif acc_type == "guest":
    print("Guest access only")
else:
    print("Unknown account")




  sjjsaaijsasas