
def driver():

    list = []

    def fib(i):
        if(i < 0):
            return 0
        if( (i == 0) or (i == 1) ):
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])

    def get_sum(n):
        for i in range (n):
            fib(i)
        sum = 0
        for i in range(n):
            sum += list[i]
        print("the sum of the first n numbers is", sum)

    n = int(input("n = "))
    get_sum(n)
    print("the sequence is", list)

if __name__ == "__main__":
    driver()