import numpy as np
from Rule import Rule

class Grid:
    
    def __init__(self, canvas, grid_size):
        self.cell_size = 10 #pixels
        self.grid_size = grid_size
        self.canvas = canvas
        self.grid = np.zeros([self.grid_size,self.grid_size], dtype=np.int)
        self.draw()
        
    def set_cell(self, x, y, state):
        if self.is_valid(x, y) == False:
            raise ValueError('Invalid coordinates x,y = ' + str(x) + ',' + str(y))
            
        self.grid[x][y] = state;
        
    def get_cell_state(self, x, y):
        if self.is_valid(x, y) == False:
            raise ValueError('Invalid coordinates x,y = ' + str(x) + ',' + str(y))
        return self.grid[x][y]
        
    def is_valid(self, x, y):
        return x < self.grid_size and x >= 0 and y < self.grid_size and y >= 0
        
    def draw(self):
        self.canvas.delete("all")
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                state_color = Rule.state_colors[self.grid[x][y]]
                self.canvas.create_rectangle(x*self.cell_size,y*self.cell_size, (x+1)*self.cell_size,(y+1)*self.cell_size, fill = state_color, outline="red")
    
     