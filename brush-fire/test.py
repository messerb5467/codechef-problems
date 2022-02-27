import networkx as nx
import logging
from .bush import Bush
from .utils import get_ints_from_string

class Test:
    def __init__(self,
                 file_context):
        self.file_context = file_context
        self.bush_graph = nx.DiGraph()
        self.fire_loop = 0
        self.__process_bush_relations()
        
    def __process_bush_relations(self):
        num_bushes, starting_burn, _ = get_ints_from_string(self.file_context.readline())
        for i in range(num_bushes):
            node_and_edge_rels = self.file_context.readline().split(" ")
            node_idx = node_and_edge_rels[0]
            edge_rels = node_and_edge_rels[1::]
            del node_and_edge_rels
 
            # Adding node_idx as part of the tuple here allows the data to be
            # less strict under the covers.
            if node_idx == starting_burn:
                self.bush_graph.add_node((node_idx, Bush(node_idx, True, False)))
            else:
                self.bush_graph.add_node((node_idx, Bush(node_idx, False, False)))
            # While the data likely uses an edge into the same node as a terminal
            # node, we won't need it for our use case since a bush can't reburn itself.
            # A burnt bush is immediately removed from the graph after being considered
            # burnt.
            bush_proximities = [(node_idx, i) for i in edge_rels if i != node_idx]
            self.bush_graph.add_edges_from(bush_proximities)
        self.sentimental_bushes = get_ints_from_string(self.file_context.readline())

    def __get_burn_status(self):
        return set([burn_status for _, burn_status in self.bush_graph.nodes(data='on_fire')])

    def __protect_bush(self):
        sentimental_bush = self.sentimental_bushes[self.fire_loop]
        bush_to_protect_node = self.bush_graph.nodes[sentimental_bush]
        ancestor = nx.algorithms.dag.ancestors(self.bush_graph, 
                                               bush_to_protect_node)
        if ancestor:
            # Current test data only allows for one ancestor node
            # to a bunch of protected bushes. Could expand on in future
            # by finding test data with multiple ancestors.
            bush_to_protect_node = ancestor[0]
        bush_to_protect_node['protect_status'] = True

    def __spread_fire(self):
        bush_fire_status = self.bush_graph.nodes.data()
        on_fire_bushes = [node for node in bush_fire_status 
                               if node.get('on_fire') == True 
                               and node.get('protect_status') == False]
        for bush in on_fire_bushes:
            close_bushes = nx.algorithms.dag.descendants(self.bush_graph, bush)
            for close_bush in close_bushes:
                if not close_bush.get('protect_status'):
                    close_bush['on_fire'] = True
        # Run with code and see if this appropriately removes
        # edges too. Documentation is not clear for this function
        # but implies it will.
        self.bush_graph.remove_nodes_from(on_fire_bushes)
    
    def __successfully_protect_bushes(self):        
        if self.bush_graph.number_of_nodes() >= len(self.sentimental_bushes) \
            and set(self.sentimental_bushes) in self.bush_graph.nodes:
            logging.info("Yes")
        elif self.bush_graph.number_of_nodes() < len(self.sentimental_bushes):
            logging.info("No")
    
    def run_burn_simulation(self):
        while(True in self.__get_burn_status()):
            self.__protect_bush()
            self.__spread_fire()
            self.fire_loop += 1            
        self.__successfully_protect_bushes()