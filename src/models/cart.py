class Cart:
    """Stores the property of a cart"""
    
    def __init__(self, capacity):
        """Initializes the cart properties"""
        self._capacity = capacity


    @property
    def capacity(self):
        """Gets cart capacity"""
        return self._capacity
