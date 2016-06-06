import json
import random as rnd
# states: 0 ... 6 -> "white",..."red"
# dirrections:
#   0 - north
#   1 - east
#   2 - south
#   3 - west
 
def save_rules(rules_map):
    json.dumps(rules_map.items())

def load_rules(dump):
    return dict(map(tuple, kv) for kv in json.loads(dump))

def get_move(rules_map, state, dx, dy):
    coord = dirr_to_coord[(dx,dy)]
    rez = rules_map[(state,coord)]
    state = rez[0]
    (dx, dy) = coord_to_dirr[rez[1]]
    return (state, dx, dy)
    
state_colors = ["white","black","red","blue","green","yellow","red"]

default_rules_map = { \
        (0,0): (1,1), (0,1): (1,2), (0,2): (1,3), (0,3): (1,0), \
        (1,0): (0,3), (1,1): (0,0), (1,2): (0,1), (1,3): (0,2) \
}
default_rules_map_dump = save_rules(default_rules_map)

coord_to_dirr = { 0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1) }
dirr_to_coord = { y: x for x,y in coord_to_dirr.iteritems() }

def generate_random_rules():
    rules = {}
    for i in range(7):
        for j in range(4):
            rules[(i,j)] = (rnd.randint(0,6), rnd.randint(0,3))
    return rules
