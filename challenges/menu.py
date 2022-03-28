
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_sub_menu = [
    ["Swap", "challenges/week0/swap.py"],
    ["Christmas", "challenges/week0/holidaybush.py"],
    ["Keypad", "challenges/week0/keypad.py"],
    ["Ship", "challenges/week0/ship.py"],
]

week1_sub_menu = [
    ["Fibonacci", "challenges/week1/fibonacci.py"],
    ["Lists", "challenges/week1/listyloopy.py"],
]

week2_sub_menu = [
    ["Factorials", "challenges/week2/factorial.py"],
    ["Factors", "challenges/week2/factors.py"],
    ["Palindrome", "challenges/week2/palindrome.py"],



]
# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nplease pick one\n{border}"
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "function menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0])
    menu_list.append(["Week 1", week1])
    menu_list.append(["Week 2", week2])
    buildMenu(title, menu_list)
# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def week0():
    title = "function submenu" + banner
    buildMenu(title, week0_sub_menu)

def week1():
    title = "Function Submenu" + banner
    buildMenu(title, week1_sub_menu)

def week2():
    title = "Function Submenu" + banner
    buildMenu(title, week2_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])
    # get user choice
    choice = input("input:")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)



        if choice == 0:
            # stop
            print("you have left the program! thank you!")
            exit()
            return

        try:
            # try as function
            action = prompts.get(choice)[1]

            action()


        except TypeError:
            try:  # try as playground style

                exec(open(action).read())



                #python_menu_challenges/ship.ship()


            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    buildMenu(banner, options)  # recursion, start menu over again
if __name__ == "__main__":
    menu()