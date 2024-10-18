from typing import List


class Node:
    def __init__(self, name: str, id: int):
        self.name: str = name
        self.id: int = id
        self.relationships: List[Node] = []

    def __str__(self):
        return f"Node(name={self.name}, id={self.id}, relationships={self.relationships})"
    
    def __repr__(self):
        return f"Node(name={self.name}, id={self.id})"