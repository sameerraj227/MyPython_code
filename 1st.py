#Typecasting in py
a="67"
b=7
c=int(a) #type conversion from str to int
sum=c+b
print("The sum of String a and int b is", sum)

#type conversion from str to float
a="6.7"
b=7
c=float(a) 
sum=c+b
print("The sum of String a and int b is", sum)

#Taking user input

a= input("Enter your name nigga: ")
print("My name is",a) 

a=float(input()) #float as input

# String

a="hello there "
print(a[0])             #output- h
print(a[1])                     #e
print(a[2])                     #l
print(a[3])                     #l
print(a[4])                     #l
print(a[5])                     #o
print(a[6])                     #_

b='''i'll print multiple alphabets using for loop'''

for chars in b:
    print(chars)

#operations in String

a='this is a tutorial'
b=len(a) #length() function
print(b)

a='this is a tutorial'
print(len(a))
#output 18

a='this is a tutorial'
print('the length of a is',len(a),'characters' )
#output- the length of a is 18 characters

#string slicer

a='the length of a is 18 characters'
print(a[0:10]) #or
print(a[:10])
#output- the length (this gave 0 to 9 character)
print(a[0:-5]) #python -ve slicing ke liye khud hi length function use kr leta hai. mtlb length of str a -5

a='mango'
print(a[0:-2])
#output- man

a='harry'
print(a[-4:-2])
#output - ar


