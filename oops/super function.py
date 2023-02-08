class Perent():
    def name(self,name):
        print("iam perent name",name)

class Child(Perent):
    def name(self):
        super().name('sree')
        print("iam child name")
obj=Child()
obj.name()