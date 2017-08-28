from model import *
from a_star import BestFirst
from graph import Graph



env = Environment((6, 6), 'envs/easy-3.txt')
graph = Graph(tuple([(car[1], car[2]) for car in env.cars]), env.get_successor_states)
searcher = BestFirst(graph, env.h, env.is_terminal_state)

i = 0
while searcher.solution is None:
    searcher.next()
    env.draw_state(searcher.last_expanded.state)
    i += 1
