from model import *
from a_star import BestFirst
from graph import Graph
import bnd


level = ['easy-3', 'medium-1', 'hard-3', 'expert-2']


env = Environment((6, 6), 'envs/'+level[3]+'.txt')
graph = Graph(tuple([(car[1], car[2]) for car in env.cars]), env.get_successor_states)
searcher = BestFirst(graph, env.h, env.is_terminal_state)

i = 0
while searcher.solution is None:
    searcher.next()
    #env.draw_state(searcher.last_expanded.state)
    i += 1
    #print(i)

print(i)
print(len(searcher.solution))
for node in searcher.solution:
    env.draw_state(node.state)
    input()



"""
env = Environment((6, 6), 'envs/medium-1.txt')
graph = Graph(tuple([(car[1], car[2]) for car in env.cars]), env.get_successor_states)
#searcher = bnd.BreadthFirst(graph, env.is_terminal_state)
searcher = bnd.DepthFirst(graph, env.is_terminal_state)


solution = searcher.solve()
print("Number of nodes expanded: #{}".format(searcher.counter))
print("Number of steps to solution: #{}".format(len(solution)))
for node in solution:
    env.draw_state(node.state)
    input()


"""