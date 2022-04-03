
def driver():
    print("hello")
    import time
    ANSI_CLEAR_SCREEN = u"\u001B[2J"
    ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
    OCEAN_COLOR = u"\u001B[44m\u001B[2D"
    SHIP_COLOR1 = u"\033[0;31m"
    SHIP_COLOR2 = u"\033[0;35m"
    SHIP_COLOR3 = u"\033[0;93m"
    RESET_COLOR = u"\u001B[0m\u001B[2D"

    def ocean_print():
        print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
        print("\n\n\n\n\n")
        print(OCEAN_COLOR + "  " * 35)


    def ship_print(position):
        print(ANSI_HOME_CURSOR)
        print(SHIP_COLOR1, end="")
        sp = " " * position
        print(sp + "    |\   ")
        print(sp + "    |/   ")
        print(SHIP_COLOR2, end="")
        print(sp + "\__ |__/ ")
        print(sp + " \__|__/ ")
        print(SHIP_COLOR3, end="")
        print(sp + "  \___/ ")
        print(RESET_COLOR)


    ocean_print()



    start = 60
    distance = -60
    step = -1


    for position in range(start, distance, step):
        ship_print(position)
        time.sleep(0.05)
