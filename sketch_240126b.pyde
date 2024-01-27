class Grid(object):
    
    def __init__(self, sqrx, sqry):
        self.ygrid = 0
        self.xgrid = 0
        self.sqrx = sqrx
        self.sqry = sqry

    def display(self):
        fill(0)
        rect(self.xgrid, self.ygrid, self.sqrx, self.sqry)
        
    def make(self):
        self.xgrid += 100
        if self.xgrid == 600:
            self.xgrid = 50
            self.ygrid += 50
            
        if self.xgrid == 550:
            self.xgrid = 0
            self.ygrid += 50
        
        if self.ygrid > height:
                self.ygrid = 0
            
        
        
    
theGrid = Grid(50, 50)
def setup():
    size(500, 500)
    
def draw():
    theGrid.display()
    theGrid.make()
