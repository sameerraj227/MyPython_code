s={1,2,4,5,454,534,True,"sam"}
print(s,type(s))
for i in s:
    print(i)


s={12,23,34,3,43,4}
a={12,43,43,4,3,74}
c=a.union(s)
b=s.intersection(a)
print(b)
print(c)
d=s.symmetric_difference(a)
print(d)
e=list(d)#list me convert
print(e)

s={5,1,23,5,55,27,3,29}
r={5,23,1,55}
print(s.isdisjoint(r))
print(s.issuperset(r))
print(r.issubset(s))