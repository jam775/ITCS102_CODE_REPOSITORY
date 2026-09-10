Sender = input("input name --->")

Type of item = int(input("input type of item ---->"))

is_Fragile = bool(input("is your item a fragile --> ?  "))

if is_Fragile == True:
	print("we will be very carefull")
else:
	print("copy that")

weight = input("input name --->")
print("that age is considered as ")


if age >= 1 and age <= 5: 
       print("infant")
elif age >= 6 and age <= 12: 
       print("kid")
elif age >= 13 and age <= 19: 
       print("teenager")
elif age >= 20 and age <= 29: 
       print("early adulthood")
elif age >= 30 and age <= 48: 
       print("adult")
elif age >= 41 and age <= 59: 
       print("advance adulthood")
elif age >= 60 and age <= 150: 
       print("senior")

else:
       print("invalid")
