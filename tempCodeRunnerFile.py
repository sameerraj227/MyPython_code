try:   
    a=int(input("enter the number: "))
    num=[32,2,4,35,45,4]
    print(num[a])
except ValueError:
    print('value entered is not a integer')

except IndexError:
    print('Index out of bound')