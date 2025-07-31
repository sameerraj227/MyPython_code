#FACTORIAL

def fact(num):
    if(num==1 or num==0):
        return(num)
    else:
        return(num*fact(num-1))
    
number=int(input("enter the number: "))
print("number ",number)
print('factorial is :', fact(number))

#FIBONACCI
def fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

num=int(input('enter the number:'))
print('fibo is:', fibo(num))