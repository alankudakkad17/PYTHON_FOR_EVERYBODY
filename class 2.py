class partyanimal:
    x=0
    name=""
    def __init__(self,nam):
        self.name=nam
        print(self.name,"constructed")
    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)
class footballfan(partyanimal):
    points=0
    def touchdown(self):
        self.points=self.points+1
        self.party()
        print(self.name,"points",self.points)
s=partyanimal("sally")
s.party()
j=footballfan("jim")
j.party()
j.touchdown()
