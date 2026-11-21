shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch or read any  anime ---? yes / no --> ").lower()

    if ans == 'yes':
        print("what kind of anime do you watch or read ---?")
        print("1- shonen \n2- korean\n3- isekai\n4- adventure\n5- fantasy")

        choice = int(input("input --> "))

        if choice == 1:
            print("SHONEN")
            title = input("Please input the title of the ANIME -->")
            shonen.append(title)
            print("list of shonen")
            print(shonen)
            con = input("Do you wish to continue yes / no ? ").lower()
            if con == "yes":
                continue
            else:
                break

        if choice == 2:
            print("KOREAN")
            title = input("Please input the title of the ANIME -->")
            korean.append(title)
            print("list of korean")
            print(korean)
            con = input("Do you wish to continue yes / no ? ").lower()
            if con == "yes":
                continue
            else:
                break
        if choice == 3:
            print("ISEKAI")
            title = input("Please input the title of the ANIME -->")
            isekai.append(title)
            print("list of isekai")
            print(isekai)
            con = input("Do you wish to continue yes / no ? ").lower()
            if con == "yes":
                continue
            else:
                break
        if choice == 4:
            print("ADVENTURE")
            title = input("Please input the title of the ANIME -->")
            adventure.append(title)
            print("list of adventure")
            print(adventure)
            con = input("Do you wish to continue yes / no ? ").lower()
            if con == "yes":
                continue
            else:
                break

        if choice == 5:
            print("FANTASY")
            title = input("Please input the title of the ANIME -->")
            fantasy.append(title)
            print("list of fantasy")
            print(fantasy)
            con = input("Do you wish to continue yes / no ? ").lower()
            if con == "yes":
                continue
            else:
                break
                
        else:
            print("INVALID CHOICE")
            
