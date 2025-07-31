#if-elif-else   
print('enter your age: ')
a=int(input())
if(a>18):
    print('you are legally authorized')
elif(a==18):
    print('learn first')
else:
    print('you are not')

#for loop

for x in range(2,10,2):
    print(x+2)

x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

name='sameer'
for i in name:
    print(i,end=" ")
    
#for list

name=["sam",'nam','abhi','lam']
for i in name:
    print(i)
    for x in i:
        print(x)

print('enter the number nigga: ')
x=int(input())
print("le apna table chutiye")
for i in range(1,11,1):
    print(x,'x',i,'=', x*i)

for x in range(3):
    for y in range(10):
        print(y,end='')
    print()

#while loop 
i=0
while(i<=3):
    print(i)
    i=i+1
print('done')

i=int(input('Enter the number :'))
while(i<30 and i>0):
    print(i)
    i=i-1
else:
    print('value out of bound')

#BREAK AND CONTINUE 
for i in range(1,20,1):
    print(i)
    if(i==19):
        break
print("done")

for i in range(1,12,1):
    if(i==11):
        print(i,'dumb')
        continue  # iske baad niche ka code skip ho jayega nd next iteration pe chala jayega
    print('end')

