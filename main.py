from model import *
from a_star import BestFirst
from graph import Graph
import bnd
from time import sleep
import time as t

level = ['easy-3', 'medium-1', 'hard-3', 'expert-2']


def run_a_star(difficulty=0, display_progress=False, time=None):
    start = t.time()
    env = Environment((6, 6), 'envs/'+level[difficulty]+'.txt')
    graph = Graph(tuple([(car[1], car[2]) for car in env.cars]), env.get_successor_states)
    searcher = BestFirst(graph, env.h, env.is_terminal_state)

    while searcher.solution is None:
        searcher.next()
        if time and display_progress:
            env.draw_state(searcher.last_expanded.state)
            sleep(time)

    print("Total number of children in search tree: {}".format(graph.n_nodes_generated))
    print("Number of nodes in graph: {}".format(len(graph.nodes)))
    print("Number of states expanded: {}".format(searcher.expand_counter))
    print("Steps to solution: {}".format(len(searcher.solution)))
    print("Runtime: {}ms".format(round((t.time() - start)*1000, 2)))
    for node in searcher.solution:
        env.draw_state(node.state)
        sleep(time)


def simple_search(algorithm, difficulty):
    algorithms = [bnd.DepthFirst, bnd.BreadthFirst]
    env = Environment((6, 6), 'envs/'+level[difficulty]+'.txt')
    graph = Graph(tuple([(car[1], car[2]) for car in env.cars]), env.get_successor_states)
    searcher = algorithms[algorithm](graph, env.is_terminal_state)

    solution = searcher.solve()
    print("Number of nodes generated: {}".format(searcher.n_nodes_generated))
    print("Number of unique nodes: {}".format(len(graph.nodes)))
    print("Number of nodes expanded: {}".format(searcher.counter))
    print("Number of steps to solution: {}".format(len(solution)))

    for node in solution:
        env.draw_state(node.state)
        input()


run_a_star(difficulty=3, time=.5, display_progress=False)
#simple_search(0, 3)
