class Edge:
    def __init__(self, node_to, sign):
        self.node_to = node_to
        self.sign = sign

    def __repr__(self):
        return "%s: to %s" % (self.sign, self.node_to)


class Node:
    def __init__(self, ordinal_number):
        self.ordinal_number = ordinal_number
        self.edges = []

    def __repr__(self):
        return "Node %s" % self.ordinal_number


class Graph:
    def __init__(self):
        self.current_node = None
        self.start_node = None
        self.end_node = None
        self.nodes = []

    def get_next_node(self, sign):
        if not self.current_node:
            return
        for edge in self.current_node.edges:
            if edge.sign == sign:
                return edge.node_to

    def reset_current_node(self):
        self.current_node = self.start_node



