row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

# this is keyboard function that prints according to the input
def keyboard(row1):
    print(row1)

    temp = row2
    row1 = temp

    print(row1)

    temp = row3
    row1 = temp

    print(row1)

if __name__ == "__main__":
    keyboard(row1)


