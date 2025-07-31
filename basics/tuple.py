tup=(1,2,3,4,34,35)
print(tup)
print(type(tup))

tup=(1,)
print(type(tup))

tup=(1,2,3,4,34,35,'great',True)
for i in tup:
    if(i==4):
        print("yes it's pertaining")
    else:
        ('no')

#                   operation in tuple

tup=(1,2,4,43,45634,5,34,'india','pak','china','bangladesh','usa','japan')
conversion=list(tup)
conversion.append('cat')
conversion.pop(7)
conversion[3]='finland'
tup=tuple(conversion)
print(tup)

tup1=(1,2,34,43)
tup2=(3,5,23,66)
print(tup1+tup2)  #concat

