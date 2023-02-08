from abc import ABC,abstractmethod
#absractmethod
class polygon(ABC):

    #abstractmethod
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract method")

class Triangle(polygon):
    def sides(self):
        print(" triangle has three side")

t=Triangle()
t.sides()
t.display()