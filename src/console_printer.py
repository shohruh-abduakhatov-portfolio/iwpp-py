###########
# Printer #
###########
class ConsolePrinter():
    """Print solution to console"""


    def __init__(self, data, routing, assignment, distance_evaluator):
        """Initializes the printer"""
        self._data = data
        self._routing = routing
        self._assignment = assignment
        self._distance_evaluator = distance_evaluator


    @property
    def data(self):
        """Gets problem data"""
        return self._data


    @property
    def routing(self):
        """Gets routing model"""
        return self._routing


    @property
    def assignment(self):
        """Gets routing model"""
        return self._assignment


    def print(self):
        """Prints assignment on console"""
        # Inspect solution.
        by_vehicle = {}
        all_nodes, all_distances = [], []
        total_dist = 0
        for cart_id in range(self.data.num_carts):
            index = self.routing.Start(cart_id)
            plan_output = 'Route for cart {0}:\n'.format(cart_id)
            nodes_list = []
            route_dist = 0
            while not self.routing.IsEnd(index):
                node_index = self.routing.IndexToNode(index)
                next_node_index = self.routing.IndexToNode(
                    self.assignment.Value(self.routing.NextVar(index)))
                route_dist += self._distance_evaluator( node_index, next_node_index)
                plan_output += ' Node {0} -> '.format(node_index)
                nodes_list.append(node_index)
                index = self.assignment.Value(self.routing.NextVar(index))
            node_index = self.routing.IndexToNode(index)
            total_dist += route_dist
            plan_output += ' Node {0} \n'.format(node_index)
            nodes_list.append(node_index)
            plan_output += 'Distance of the route: {0}m\n'.format(route_dist)
            if route_dist == 0: continue
            all_nodes.append(nodes_list)
            all_distances.append(route_dist)
            by_vehicle[cart_id] = {
                'nodes': nodes_list,
                'distance': route_dist
            }
            print(plan_output)
        print('Total Distance of all routes: {0}m'.format(total_dist))
        res_dict = {
            'by_vehicle': by_vehicle,
            'total_distance': total_dist,
            'by_route': {
                'nodes': all_nodes,
                'distances': all_distances
            }
        }
        return res_dict
