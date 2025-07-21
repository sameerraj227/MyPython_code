s={'Name':'SAMEER RAJ','age':21,'class':9,'Eligible':True}
print(s,type(s))
print(s.get('age'))
print(s['Name'])
print(s.keys())
print(s.values())

#printing KEYS using for loop
for i in s:
    print(i)

#printing values using loops

for i in s.keys():
    print(s[i])

print(s.items())

#                                               methods

info = {'name':'Karan', 'age':19, 'eligible':True}
info2 = {'name':'sulek', 'age':21, 'eligible':False}
info.update(info2)
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
info.pop('age')
print(info)
info.clear()
print(info)

#looping technique

info = {'name':'Karan', 'age':19, 'eligible':True}
info2 = {'name':'sulek', 'age':21, 'eligible':False}

for i,j in info.items():
    print(i,':',j)


for i in range(6):
    print(i)
    if(i==4):
        break 
else:print('sorry')

nums = [2, 4, 6, 8]

for n in nums:
    if n % 2 != 0:
        print("Found odd number")
        break
else:
    print("All numbers are even ✅")
