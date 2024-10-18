from Node import Node
from NodeRelationship import NodeRelationship
from typing import List
from random import choices, randint, sample
from string import ascii_letters

class NodePool:
    def __init__(self, nodecount: int):
        self.nodes: List[Node] = [Node("".join(choices(ascii_letters, k=6)), i) for i in range(nodecount)]
        for i in range(nodecount):
            relcount = randint(1, 5)
            relationships = sample(self.nodes, k=relcount)
            while self.nodes[i] in relationships:
                relationships = sample(self.nodes, k=relcount)
            self.nodes[i].relationships = relationships

    def generate_relationship_values(self):
        relationship_values = []
        for i in self.nodes:
            rel_vals = []
            for j in i.relationships:
                if i not in j.relationships and NodeRelationship(i, j, 0) not in relationship_values:
                    relationship_values.append(NodeRelationship(i, j, 0))
                    continue
                elif i in j.relationships and NodeRelationship(i, j, (1/((i.relationships.index(j)+1)*(j.relationships.index(i)+1)))):
                    relationship_values.append(NodeRelationship(i, j, (1/((i.relationships.index(j)+1)*(j.relationships.index(i)+1)))))
        return relationship_values
