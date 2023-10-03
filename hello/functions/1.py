import re
Password= input("Enter password")
i = True
while i:  
    if (len(Password)<6 or len(Password)>12):
        break
    elif not re.search("[a-z]",Password):
        break
    elif not re.search("[0-9]",Password):
        break
    elif not re.search("[A-Z]",Password):
        break
    elif not re.search("[$#@]",Password):
        break
    elif re.search("\s",Password):
        break
    else:
        print("Valid")
        i=False
        break

if i:
    print("Not Valid")
