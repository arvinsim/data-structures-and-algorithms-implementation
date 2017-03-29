class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
        
    def getWeight(self, nbr):
        if nbr in self.connectedTo:
            return self.connectedTo[nbr]
        return None

    
if __name__ == '__main__':
    v0 = Vertex(0)
    v0.addNeighbor('v1', 1)
    v0.addNeighbor('v2', 2)

    print(v0.getConnections())
    print(v0.getId())
    print(v0.getWeight('v2'))
