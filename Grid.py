import numpy as np
import Rules
import random as rnd

class Grid:
    
    def __init__(self, canvas, grid_size):
        self.cell_size = 10 #pixels
        self.grid_size = grid_size
        self.generate_random_agents(5)
        self.canvas = canvas
        self.grid = np.zeros([self.grid_size,self.grid_size], dtype=np.int)
        self.draw()
        
    def generate_diagonal_agents(self, nr_agents):
        self.ants = []
        self.rules = []
        for i in range(nr_agents):
            range_start = i * self.grid_size / nr_agents
            range_end = (i + 1) * self.grid_size / nr_agents - 1
            pos_x = rnd.randint(range_start,range_end)
            pos_y = rnd.randint(range_start,range_end)
            self.ants.append(Ant(pos_x , pos_y))
            self.rules.append(Rules.generate_random_rules())
            
    def generate_random_agents(self, nr_agents):
        self.ants = []
        self.rules = []
        for i in range(nr_agents):
            pos_x = rnd.randint(0, self.grid_size - 1)
            pos_y = rnd.randint(0, self.grid_size - 1)
            self.ants.append(Ant(pos_x , pos_y))
            self.rules.append(Rules.generate_random_rules())
            
    def generate_full_agents(self):
        self.ants = []
        self.rules = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.ants.append(Ant(i , j))
                self.rules.append(Rules.generate_random_rules())
            
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
        
    def step(self, agent_index):
        ant = self.ants[agent_index]
        rule = self.rules[agent_index]
        current_state = self.get_cell_state(ant.x, ant.y)
        state, dx, dy = Rules.get_move(rule, current_state, ant.dx, ant.dy)
        if self.is_valid(ant.x + dx, ant.y + dy):
            ant.dx = dx
            ant.dy = dy
            self.set_cell(ant.x, ant.y, state)
            ant.x += dx
            ant.y += dy
            
    def step_all(self):
        for i in range(len(self.ants)):
            self.step(i)
        
    def restart(self):
        self.grid = np.zeros([self.grid_size,self.grid_size], dtype=np.int)
        self.generate_random_agents(40)
        self.draw()
        
    def draw(self):
        self.canvas.delete("all")
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                state_color = Rules.grayscale_state_colors[self.grid[x][y]]
                hex_color = '#%02x%02x%02x' % (state_color, state_color, state_color)
                self.canvas.create_rectangle(x*self.cell_size,y*self.cell_size, (x+1)*self.cell_size,(y+1)*self.cell_size, fill = hex_color, outline="red")
    
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 0