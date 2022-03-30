#See hack 1 above, InfoDB lists
#See hack 2 above, InfoDB loops
def tester():
    # List with dictionary records placed in a list
    InfoDb = []

    InfoDb.append({
        "FirstName": "Sanvi",
        "LastName": "Pal",
        "Favorite Number": "8",
        "Age": "18",
        "Favorite Color": "lilac",
        "Favorite_subjects":["CSP", "Discrete", "Stats", "Gov"]
    })

    InfoDb.append({
        "FirstName": "John",
        "LastName": "Mortensen",
        "Favorite Number": "21",
        "Age": "30",
        "Favorite Color": "blue",
        "Favorite_subjects":["Math", "Science", "English", "Art"]
    })

    InfoDb.append({
        "FirstName": "Sunny",
        "LastName": "Naidu",
        "Favorite Number": "2",
        "Age": "30",
        "Favorite Color": "purple",
        "Favorite_subjects":["A","B","C"]
    })


    def print_data(n):
        print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
        print("\t", "Classes: ", end="")
        print(", ".join(InfoDb[n]["Favorite_subjects"]))
        print()

    #for loop
    #Python For Loops
    #iterates over a sequence for a set number of times
    #The range() Function:
    #returns a sequence of numbers


    def for_loop():
        for n in range(3):
            print_data(n)

    print("for loop")
    for_loop()

    #while loop
    #statements execute until the required statements change logic (t/f)
    def while_loop():
        n = 0
        while n < 3:
            print_data(n)
            n += 1

    print("while loop")
    while_loop()

    #recursive loop
    #calls itself.
    #needs to have exit condition

    def recursive_loop(n):
        if n < len(InfoDb):
            print_data(n)
            n +=1
            recursive_loop(n)
        return

    print("recursive loop")
    recursive_loop(0)


tester()


