age1 = 16
age2 = 21

def swap(age1,age2):

    print(age1, age2)

    temp = age1
    age1 = age2
    age2 = temp

    print(age1,age2)

if __name__ == "__main__":
    swap(age1,age2)
