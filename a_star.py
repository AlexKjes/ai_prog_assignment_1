from graph import Node





class BestFirst:

    def __init__(self, graph, h_fn, solution_fn):
        self.h_fn = h_fn
        self.solution_fn = solution_fn

        self.graph = graph
        node = graph.get_start_node()
        node.g = 0
        node.h = h_fn(node.state)

        self.frontier = [graph.get_start_node()]
        self.last_expanded = None
        self.solution = None

    def next(self):



    def get_next_best_node(self):
        best_node = self.frontier[0]
        best_w = best_node.g + best_node.h
        for n in self.frontier:
            nw = n.g + n.h
            if nw < best_w:
                best_w = nw
                best_node = n
        return best_node







