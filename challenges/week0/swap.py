age1 = 32
age2 = 18

def swap(age1=32, age2=18, t=age1):
    print('You chose Swap')
    if age1 > age2:
        age1 = age2
        age2 = t
    return age1, age2

print(swap())

print(age1,age2)