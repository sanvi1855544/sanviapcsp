age1 = 21
age2 = 18

def swap(age1=21, age2=18, temp=age1):
    print('You chose \' 1 -  Swap\'')
    if age1 > age2:
        age1 = age2
        age2 = temp
    return age1, age2

print(swap())
print(age1,age2)