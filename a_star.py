from graph import Node











class BestFirst:

    def __init__(self, init_state, h_fn, unpack_fn, solution_fn):
        self.unpack_fn = unpack_fn
        self.h_fn = h_fn
        self.solution_fn = solution_fn

        self.visited = {}
        self.frontier = {Node(init_state, 0, h_fn(init_state))}
        self.last_expanded = None
        self.solution = None

    def next(self):
            w_high = self.frontier[0].get_weight()
            high_index = 0
            for n in self.frontier:
                n_weight = n.get_weight()
                if n_weight < w_high:
                    w_high = n_weight
                    high_index = i
            next_node = self.frontier.
            #print(next_node.get_weight())
            self.last_expanded = next_node
            if self.solution_fn(next_node.state):
                self.solution = [next_node.state]
                while next_node.parent is not None:
                    self.solution.insert(0, next_node.parent)
                    next_node = next_node.parent
                return
            self.visited[next_node.state] = next_node
            ### TODO implement duplicate guard
            for s in self.unpack_fn(next_node.state):
                new_node = Node(s, next_node.g + 1, self.h_fn(s), next_node)
                if new_node not in self.visited or self.visited[s].g > new_node.g:
                    self.frontier.append(new_node)
                next_node.children.append(new_node)


    def check_duplicate_state(self, node):
        if node.state in self.visited and self.visited[node.state].g > node.g:
            self.update_g(node, no)

    def update_g(self, node, new_g):
        if node.g > new_g:
            node.g = new_g
            for child in node.children:
                self.update_g(child, new_g + 1)



