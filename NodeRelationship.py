from Node import Node

class NodeRelationship:
    def __init__(self, node1: Node, node2: Node, score: float):
        self.node1 = node1
        self.node2 = node2
        self.score = score

    def __eq__(self, other):
        if(type(other) != NodeRelationship):
            return False
        if {other.node1, other.node2} == {self.node1, self.node2} and self.score == other.score:
            return True
        return False
    
    def __lt__(self, other):
        if self.score < other.score:
            return True
        return False
    
    def __str__(self):
        return f"NodeRelationship(node1={self.node1.__repr__()}, node2={self.node2.__repr__()}, score={self.score})"
    
    __repr__ = __str__