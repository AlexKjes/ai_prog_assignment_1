


class BreadthFirst:

    def __init__(self, graph, solution_fn):
        self.graph = graph
        self.queue = [graph.get_start_node()]
        self.solution_fn = solution_fn
        self.counter = 0

    def solve(self):
        while True:
            current_node = self.queue.pop()
            if self.solution_fn(current_node.state):
                break
            self.counter += 1
            for child in current_node.get_children():
                if not child.is_expanded:
                    child.prev = current_node
                    self.queue.insert(0, child)
            current_node = self.queue.pop()
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

    def solve(self):
        current_node = self.stack.pop()
        current_node.prev = None
        while not self.solution_fn(current_node.state):
            self.counter += 1
            for child in current_node.get_children():
                if not child.is_expanded:
                    child.prev = current_node
                    self.stack.append(child)
            current_node = self.stack.pop()
        ret = []
        while current_node.prev is not None:
            ret.insert(0, current_node)
            current_node = current_node.prev
        return ret
