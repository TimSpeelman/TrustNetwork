from random import choice, random



from networkx import get_node_attributes, random_geometric_graph, pagerank, draw_networkx_edges, draw_networkx_nodes

from matplotlib import pyplot

n = 500
R = 5
c = 0.1

G = random_geometric_graph(n, 0.1)
pos = get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
d_min = 1
n_center = 0

for n in pos:
    x, y = pos[n]
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d < d_min:
        n_center = n
        d_min = d

pr = pagerank(G)
pyplot.figure(figsize=(8, 8))
draw_networkx_edges(G, pos, nodelist=[n_center], alpha=0.4)
draw_networkx_nodes(G, pos, nodelist=list(pr.keys()),
                    node_size=80,
                    node_color=list(pr.values()),
                    cmap='Reds')

pyplot.xlim(-0.05, 1.05)
pyplot.ylim(-0.05, 1.05)
pyplot.axis('off')
pyplot.show()

node_walks = list()
for node in G.nodes():
    walks = list()
    for i in range(R):
        walk = list()
        next_node = choice(G.neighbors(node))
        walk.append(next_node)
        while random() > c:
            walk.append(next_node)
            next_node = choice(G.neighbors(next_node))
        walks.append(walk)
    node_walks.append(walks)

counts = dict()
for node in G.nodes():
    counts[node] = 0
    for walks in node_walks:
        for walk in walks:
            counts[node] += walk.count(node)

total = sum(counts.values())
print("Expected: {n * R / c}, actual: {total}")
for key, value in counts.items():
    counts[key] = value / total
print(counts)

print()