class Rule:
    state_colors = ["white","black","red","blue","green","yellow","red"]
    max_states = 7
    
    def __init__(self, nr_states):
        if nr_states > Rule.max_states:
            raise ValueError('nr_states exceeds max value of ' + max_states)
            
        self.nr_states = nr_states
    
    def get_move(self, state, dx, dy):
        if state == 0:
            if dx != 0:
                dy = dx
                dx = 0
            else:
                dx = (-1) * dy
                dy = 0
        else:
            if dx != 0:
                dy = (-1) * dx
                dx = 0
            else:
                dx = dy
                dy = 0
        return ((state + 1) % self.nr_states, dx, dy)
        