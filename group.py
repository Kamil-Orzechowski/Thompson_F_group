class FGroupElement:
    def __init__(self, vertices):
        self.vertices = tuple(vertices)
        self.dom_subdivision = tuple([v[0] for v in self.vertices])
        self.img_subdivision = tuple([v[1] for v in self.vertices])

    def get_slopes(self):
        return [(self.vertices[i + 1][1] - self.vertices[i][1])
                / (self.vertices[i + 1][0] - self.vertices[i][0])
                for i in range(len(self.vertices) - 1)]
