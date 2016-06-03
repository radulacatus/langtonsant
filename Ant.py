class Ant:
    
    def __init__(self, x, y, grid, rule):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 0
        self.rule = rule
        self.grid = grid
        
    def step(self):
        current_state = self.grid.get_cell_state(self.x, self.y)
        state, dx, dy = self.rule.get_move(current_state, self.dx, self.dy)
        if self.grid.is_valid(self.x + dx, self.y + dy):
            self.dx = dx
            self.dy = dy
            self.grid.set_cell(self.x, self.y, state)
            self.x += dx
            self.y += dy
        