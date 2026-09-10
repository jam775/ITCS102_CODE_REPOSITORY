Sender = input("input name --->")

Type_of_item = input("input type of item ---->")

is_Fragile = bool(input("is your item a fragile? (True or False) --->"))
if is_Fragile == "True":
    print("we will be very carefull")
    
else:
    print("copy that")

weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
is_Express = bool(input("Is it express? (True or False)"))
is_international = bool("Is it international? (True or False?-->)")

base_cost = (weight * 2.50) + (distance * 0.15)

if weight < 2.0 and distance <= 100 and not is_Express and not is_international:
    total = 0.00
	
elif is_international and is_Express:
    total = (base_cost * 1.40) + 50

elif is_Express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    print("total base_cost")
    













