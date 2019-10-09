class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node, visited=None):
    #build our graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        #build edges in reverse
        graph.add_edges(pair[1], pair[0])

    qq = Queue()
    qq.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1]

        if(len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = vertex
            max_path_length = len(path)

        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            qq.enqueue(path_copy)

    return earliest_ancestor