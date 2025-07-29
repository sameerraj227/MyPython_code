class Person:
    name="harry"
    occupation="student"
    salary=1000

    def info(self):
        return f"{self.name} is a {self.occupation} earning {self.salary}"

a=Person()
b=Person()
c=Person()
a.name="John"
a.occupation="teacher"
a.salary=2000
print(a.info())