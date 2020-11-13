def manhattan_distance(position_1, position_2):
    """Computes the Manhattan distance between two points"""
    return (abs(position_1[0] - position_2[0]) +
            abs(position_1[1] - position_2[1]))


class CreateDistanceEvaluator(object):  # pylint: disable=too-few-public-methods
    """Creates callback to return distance between points."""


    def __init__(self, data, distance_calculator):
        """
        Initializes the distance matrix
        :param data:
        :param distance_calculator: pre_calced_distances from pickle file
        """
        self._data = data
        self._distances = distance_calculator


    def distance_evaluator(self, from_node, to_node):
        """Returns the manhattan distance between the two nodes"""
        from_node_str = str(self._data.locations[from_node]).replace(r', ', '_').strip('[]').strip('()')
        to_node_str = str(self._data.locations[to_node]).replace(r', ', '_').strip('[]').strip('()')
        return self._distances[from_node_str][to_node_str]['distance']
