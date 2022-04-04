from subprocess import call
from lists import listyloopy
from mymath import factorial, factors, keypad, swap
from patterns import fib, holidaybush, palindrome, ship

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_sub_menu = [
    ["Swap", swap.driver],
    ["Christmas", holidaybush.driver],
    ["Keypad", keypad.driver],
    ["Ship", ship.driver],
]

week1_sub_menu = [
    ["Fibonacci", fib.driver],
    ["Lists", listyloopy.driver],
]

week2_sub_menu = [
    ["Factorials", factorial.driver],
    ["Factors", factors.driver],
    ["Palindrome", palindrome.driver],
]

border = "=" * 25
banner = f"\n{border}\nplease pick one\n{border}"


def menu():
    title = "function menu" + banner
    menu_list = main_menu.copy()
    menu_list.append([bcolors.OKBLUE + "Week 0" + bcolors.ENDC, week0])
    menu_list.append([bcolors.OKGREEN + "Week 1" + bcolors.ENDC, week1])
    menu_list.append([bcolors.OKCYAN + "Week 2" + bcolors.ENDC, week2])

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
  call(["python", "challenges/animation.py"])  
  menu()