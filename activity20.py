from getpass import getpass

u = "jam"
pword = "jamaganda"

islogin = False

while islogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == u and password == pword:
        print("Login successfully")
        islogin = True
    else:
        print("ACCESS DENIED")