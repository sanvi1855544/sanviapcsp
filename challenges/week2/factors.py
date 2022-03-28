##challenge 2 entails coding math function
##used mr. M's ideas and code is a factors algo

def tester():
    class factors:
        def __init__(self):
            return
        def __call__(self, n):
            if isinstance(n, int) == True and 0 < n and n < 10000:
                x = n
                t_list = []
                f_list = []
                for i in range(x):
                    while 0 < x:
                        t_list.append(x)
                        x = x - 1
                #print(temporary list) all the numbers before n
                for i in range(n):
                    if n % t_list[i] == 0:
                        f_list.append(t_list[i])
                return f_list
            else:
                print("input was not valid: ")
                return"null"
    f_obj = factors()

    print("1 factorial = ",f_obj(1))
    print("5 factorial = ",f_obj(50))
    print("50 factorial = ",f_obj(1000))
    print("0 factorial = ",f_obj(0)) #no 0
    print("-5 factorial = ",f_obj(-50)) #no negative numbers
    print("20000000000 factorial = ",f_obj(20000000000)) #too large
    print("77.8 factorial = ",f_obj(77.8)) #no decimals allowed
    print("A factorial = ",f_obj("A"))  #no alphabets allowed

tester()
