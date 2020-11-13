class DataProblem():
    """Stores the data for the problem"""


    def __init__(self, num_carts, locations):
        """Initializes the data for the problem"""
        self._locations = locations
        self._depot = 0 # packing zone index
        self._num_carts = num_carts


    @property
    def num_carts(self):
        """Gets number of carts"""
        return self._num_carts


    @property
    def locations(self):
        """Gets locations"""
        return self._locations


    @property
    def num_locations(self):
        """Gets number of locations"""
        return len(self.locations)


    @property
    def depot(self):
        """Gets depot location index"""
        return self._depot
