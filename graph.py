class Graph:

    def __init__(self, start_node, node_expander):

        self.node_expander = node_expander
        self.nodes = {start_node: self.Node(self, start_node)}

    def get_start_node(self):
        return self.nodes[self.nodes.keys()[0]]

    class Node:
        def __init__(self, graph, state):
            self._graph = graph

            self.state = state

            self.parents = []
            self._children = []
            self.is_expanded = False

        def get_children(self):
            if not self.is_expanded:
                self.is_expanded = True
                self._expand()
            return self._children

        def _expand(self):
            children = self._graph.node_expander(self.state)
            for child in children:
                if child in self._graph.nodes:
                    self._graph.nodes[child].parents.append(self)
                    self._children.append(self._graph.nodes[child])
                else:
                    cn = Graph.Node(self._graph, child)
                    cn.parents.append(self)
                    self._graph.nodes.append(cn)
                    self._children.append(cn)



