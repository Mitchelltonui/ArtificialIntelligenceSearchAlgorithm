#GROUP 4 ADAH NYAMWANGE -110695 , MITCHELL TONUI -111053 , DAVID OGALO - 110946
import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","J1","Phase3","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Mada","ParkingLot",weight="700")
#position the nodes to resemble Madaraka map
G.nodes["Ph.1B"]['pos']=(0,0)
G.nodes["Ph.1A"]['pos']=(6,3)
G.nodes["STC"]['pos']=(0,-2)
G.nodes["Phase2"]['pos']=(2,0)
G.nodes["J1"]['pos']=(6,0)
G.nodes["Mada"]['pos']=(10,0)
G.nodes["SportsComplex"]['pos']=(-3,2)
G.nodes["Siwaka"]['pos']=(0,2)
G.nodes["Phase3"]['pos']=(3,-2)
G.nodes["ParkingLot"]['pos']=(3,-3)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
