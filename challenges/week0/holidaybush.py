
def tree():
    print('You chose Tree')
    for i in range(10):
        for j in range(10-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()


    c = "****"
    spaces = "                  "
    stem = spaces + c
    for i in range(3):
        print(stem)

tree()