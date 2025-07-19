def isGreater(a,b):
    return max(a,b)

a=int(input("enter first num: "))
B=int(input("enter Second num: "))
c=isGreater(a,B)
print(c)

#or

def isGreater(a,b):
    if(a>b):
        print('a is greater')
    else:
        print('b is greater')
a=int(input("enter first num: "))
B=int(input("enter Second num: "))
isGreater(a,B)


a=int(input("enter first num: "))
B=int(input("enter Second num: "))
c=max(a,B)       #BUILT IN FUNCTION
print('THE GREATER NUMBER IS ',c)


a=int(input("enter first num: "))
B=int(input("enter Second num: "))
c=sum([a,B])       #BUILT IN FUNCTION and sum() needs an iterable (like list or tuple)
print('THE sum of NUMBER IS',c)

#                                                    function args
#1  default args
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")

#keyword arbitary args
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker",fname='sue' )

#required args
def name(fname, mname, lname):
    print("Hello,", fname,lname,  mname)
name("Peter", 'raj',"Quill")

#return type

def sumNum(*number):
    sum=0
    for i in number:
        sum=sum+i
    return sum/len(number)
c=sumNum(3,5,7,45,3,8)
print(c)

