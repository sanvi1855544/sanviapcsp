
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_sub_menu = [
    ["Swap", "challenges/math/swap.py"],
    ["Christmas", "challenges/patterns/holidaybush.py"],
    ["Keypad", "challenges/math/keypad.py"],
    ["Ship", "challenges/patterns/ship.py"],
]

week1_sub_menu = [
    ["Fibonacci", "challenges/math/fib.py"],
    ["Lists", "challenges/lists/listyloopy.py"],
]

week2_sub_menu = [
    ["Factorials", "challenges/math/factorial.py"],
    ["Factors", "challenges/math/gcd.py"],
    ["Palindrome", "challenges/patterns/palindrome.py"],



]

border = "=" * 25
banner = f"\n{border}\nplease pick one\n{border}"


def menu():
    title = "function menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0])
    menu_list.append(["Week 1", week1])
    menu_list.append(["Week 2", week2])
    buildMenu(title, menu_list)


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
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("input:")

    try:
        choice = int(choice)



        if choice == 0:
            # stop
            print("you have left the program! thank you!")
            exit()
            return

        try:
            action = prompts.get(choice)[1]

            action()


        except TypeError:
            try:

                exec(open(action).read())


            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)
if __name__ == "__main__":
    menu()