


class BreadthFirst:

    def __init__(self, graph, solution_fn):
        self.graph = graph
        self.queue = [graph.get_start_node()]
        self.solution_fn = solution_fn
        self.counter = 0
        self.n_nodes_generated = 0
        self.seen = [self.queue[0].state]

    def solve(self):
        while True:
            current_node = self.queue.pop()
            if self.solution_fn(current_node.state):
                break
            self.counter += 1
            for child in current_node.get_children():
                self.n_nodes_generated += 1
                if child.state not in self.seen:
                    self.seen.append(child.state)
                    child.prev = current_node
                    self.queue.insert(0, child)
        ret = []
        while True:
            ret.insert(0, current_node)
            current_node = current_node.prev
            if not hasattr(current_node, 'prev'):
                break
        return ret


class DepthFirst:
    def __init__(self, graph, solution_fn):
        self.graph = graph
        self.stack = [graph.get_start_node()]
        self.solution_fn = solution_fn
        self.counter = 0
        self.n_nodes_generated = 0
        self.seen = [self.stack[0].state]

    def solve(self):
        current_node = self.stack.pop()
        current_node.prev = None
        while not self.solution_fn(current_node.state):
            self.counter += 1
            for child in current_node.get_children():
                self.n_nodes_generated += 1
                if child.state not in self.seen:
                    child.prev = current_node
                    self.seen.append(child.state)
                    self.stack.append(child)
            current_node = self.stack.pop()
        ret = []
        while current_node.prev is not None:
            ret.insert(0, current_node)
            current_node = current_node.prev
        return ret
