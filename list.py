marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive i

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

l=[i for i in range(20) if i%2==0]
print(l)

#                               list methods
l=[1,23,4,5,3,45,6,34,5,38,63,4]
l.sort()#will sort
print(l)

l.reverse()#will reverse the entire list
print(l)

l.sort(reverse=True)#will print in descending
print(l)

print(l.index(4))#will give the 4th index element 

l.append(77)#will add 77 in the end of the list
print(l)

l.insert(6,99)#will insert 99 at 6th index
print(l)

print(l.count(4))#will count the number to 4

l.remove(38)#element 38 will be removed
print(l)

l.pop(4)# index 4 element
print(l)

l.clear()#will clear the whole list
print(l)

m=list.copy(l)#will copy list l
m[0]=11
print(m)