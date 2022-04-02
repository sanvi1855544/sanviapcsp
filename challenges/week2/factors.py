def driver():
    class factors:
        def __init__(self):
            return
        def __call__(self, n):
            if isinstance(n, int) == True and 0 < n and n < 10000:
                x = n
                temp_list = []
                final_list = []
                for i in range(x):
                    while 0 < x:
                        temp_list.append(x)
                        x = x - 1
                #print(temp_list) all the numbers before n
                for i in range(n):
                    if n % temp_list[i] == 0:
                        final_list.append(temp_list[i])
                return final_list
            else:
                print("input was not valid: ")
                return"null"
    factors_obj = factors()

    print("1 factorial = ",factors_obj(1))
    print("6 factorial = ",factors_obj(60))
    print("50 factorial = ",factors_obj(1000))
    print("0 factorial = ",factors_obj(0)) #no 0
    print("-1 factorial = ",factors_obj(-1)) #no negative numbers
    print("20000000000 factorial = ",factors_obj(20000000000)) #too large
    print("45.3 factorial = ",factors_obj(45,3)) #no decimals allowed
    print("A factorial = ",factors_obj("S"))  #no alphabets allowed

if __name__ == "__main__":
    driver()