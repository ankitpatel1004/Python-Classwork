class Pen:

    def __init__(self,price,color,company):
        self.price = price
        self.color = color
        self.company = company
    def display(self):
        print(self.price,self.color,self.company)

class Notebook(Pen):

    def __init__(self,price,color,company,pages):
        self.pages = pages
        super().__init__(price, color, company)

    def display(self):
        print(self.price,self.color,self.company,self.pages)

p = Pen(30,"Green","Cello")
p.display()

n = Notebook(40,"Blue","Monster",400)
n.display()
