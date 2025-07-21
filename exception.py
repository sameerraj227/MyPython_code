try:   
    a=int(input("enter the number: "))
    num=[32,2,4,35,45,4]
    print(num[a])
except ValueError:
    print('value entered is not a integer')
except IndexError:
    print('Index out of bound')

def evennum(a,b):
    even=[]
    for i in range(a,b):
                        if i%2==0:
                            even.append(i)
    return even
a=int(input("enter the starting number:"))
b=int(input("enter the ending number:"))
eve=evennum(a,b)
print(eve)



#                                   raising Custom Errors

a=int(input("enter the number: "))
if a<0 or a>100:
    raise ValueError("Number must be between 0 and 100")
else:
    print("Number is within the range")

a=input('enter the string: ')
if not a.isalpha():
    raise TypeError("Input must be a string containing only letters")


a = input("Enter the string: ")
for i in a[::-1]:
    print(i, end=' ')
