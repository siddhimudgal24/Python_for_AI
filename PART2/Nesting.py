# Login system

username = input("Enter Username:")
password = input("Enter Password:")

if(username=="admin" and password =="pass") :
    print("login successful")
else:
    if username !="admin": #Nesting
        print("wrong username,try again.")
    else: 
        print("wrong password,try again.")