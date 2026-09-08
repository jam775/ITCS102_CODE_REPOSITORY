import getpass

username = 'user1'
password = 'pogiako123'

u = input('Input Username ---> ')
p = getpass.getpass('Input password ---> ')

if username == u and p == password :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")