class students():

    def details(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name)
        print(self.age)
        print(self.place)

x = students()
y = students()
x.details('sreejesh',23,'pala')
y.details('arun',22,'ekm')
x.display()
print("----------------")
y.display()


