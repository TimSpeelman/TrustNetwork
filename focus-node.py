from random import choice, random
import networkx as nx
from networkx import get_node_attributes, random_geometric_graph, pagerank, draw_networkx_edges, draw_networkx_nodes
from matplotlib import pyplot

G = nx.Graph()
pos=[(2,2),(1,1),(2,3),(3,1)]; # positions for all nodes

fig = pyplot.figure()
ax = fig.add_subplot(111)
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0],
                       node_color='r',
                       node_size=800)
nx.draw_networkx_nodes(G, pos,
                       nodelist=[1,2,3],
                       node_color='b',
                       node_size=500)

nx.draw_networkx_edges(G, pos, [(0,1),(0,2),(0,3)])

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))

    nx.draw_networkx_nodes(G, [(event.x, event.y)],
                           nodelist=[0],
                           node_color='y',
                           node_size=800)
    pyplot.show()


cid = fig.canvas.mpl_connect('button_press_event', onclick)

pyplot.show()