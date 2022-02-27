import networkx
from bush import Bush

class Test:
    def __init__(self,
                 bush_graph):
        self.bush_graph = bush_graph

    def process_bush_relations(file,
                               bush_graph,
                               num_bushes,
                               starting_burn):
      for i in range(num_bushes):
          node_and_edge_rels = file.readline().split(" ")
          node_idx = node_and_edge_rels[0]
          edge_rels = node_and_edge_rels[1::]
          del node_and_edge_rels
 
          # Adding node_idx as part of the tuple here allows the data to be
          # less strict under the covers.
          if node_idx == starting_burn:
              bush_graph.add_node((node_idx, Bush(node_idx, True, False)))
          else:
              bush_graph.add_node((node_idx, Bush(node_idx, False, False)))
          # While the data likely uses an edge into the same node as a terminal
          # index of sort, we won't need it for our use case.
          bush_proximities = [(node_idx, i) for i in edge_rels if i != node_idx]
          bush_graph.add_edges_from(bush_proximities)

    def spread_fire(bush_graph):
        bush_fire_status = bush_graph.nodes.data()
        on_fire_bushes = [node for node in bush_fire_status 
                               if node.get('fire_status') == True 
                               and node.get('protect_status') == False]
        for bush in on_fire_bushes:
        close_bushes = nx.algorithms.dag.descendants(bush_graph, bush)
        for close_bush in close_bushes:
            close_bush['fire_status'] = True
        # Run with code and see if this appropriately removes
        # edges too. Documentation is not clear for this function
        # but implies it will.
        bush_graph.remove_nodes_from(on_fire_bushes)

    def protect_bush(bush_graph,
                 sentimental_bushes):
        bush_to_protect = sentimental_bushes.pop(0)
        bush_graph.nodes[bush_to_protect]['protect_status'] = True