from NodePool import NodePool

pool = NodePool(100)

a = pool.generate_relationship_values()

a.sort()

print(a[::-1])