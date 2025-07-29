def double(x):
    return x * 2

print(double(5))
print(double(10))
print(double(15))

a=lambda x,y,z:(x + y + z) / 3
print(a(10, 20, 30))

#                                                                                  class

class Person:
    name="harry"
    occupation="student"
    salary=1000

    def info(self):
        return f"{self.name} is a {self.occupation} earning {self.salary}"

a=Person()
a.name="John"
a.occupation="teacher"
a.salary=2000
print(a.info())
