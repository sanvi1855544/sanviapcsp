def christmastree(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1


if __name__ == "__main__":
    christmastree(5)