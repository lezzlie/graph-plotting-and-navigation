from heapq import heapify, heappush, heappop
import matplotlib.pyplot as plt
import networkx as nx

def show_graph(G, custom_node_positions=None, node_labels=None): #G is the graph we want to display when calling this function.
    plt.figure() # this function creates a new indow or 'figure' to draw the graph.
    if custom_node_positions== None:
        pos = nx.spring_layout (G) # this funtion uses networkX's spring layout in order to calculate where each node should be plotted
        #if the custom_node_positions variable has not been provided, the provided G variable will be used to automaticcally position the nodes. 
    else :
      pos=custom_node_positions # else the custom node positions will be used.


    weight_labels = nx.get_edge_attributes(G, 'weight')  # this obtains the weight attributes for evey edge of the graph.
    nx.draw(G, pos, font_color='white' , node_shape = 's', with_labels = True , ) #draws the graph.
    output = nx.draw_networkx_edge_labels(G,pos, edge_labels=weight_labels) # adds the edge weights. 
    #you can use pos for multiple drawing functions, the function tself will work out where to plot it, mathmatically in relation the the positioning of the nodes.
    if node_labels!=None: 
        pos2 = {k: (v[0] + 0.05) for (k,v) in pos.items()} 
        nx.draw_networkx_labels(G, pos2, labels-node_labels, font_color='r')


G = nx.DiGraph() #created a directed graph and saves it as G

G.add_weighted_edges_from([
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8)
]) # adds nodes between A, B, C and D with weights connecting them. 
#when using the .add_weighted_edges_from method, the first two elements of each tuple are the nodes and the third element is the weight of the edge connecting them, so it looks like (node1, node2, weight).
#this will be important when using the get_edge_attributes method to get the weights of the edges for display on the graph.

show_graph(G) # calls the graph function to draw the graph
plt.show() #displays th graph 
