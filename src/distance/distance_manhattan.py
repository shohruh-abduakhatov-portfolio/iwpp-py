class ManhattanDistance:

    @staticmethod
    def manhattan(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


    # this is one working method
    @staticmethod
    def calc_manhattan(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


    @staticmethod
    def distance_calculator(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


    def __init__(self) -> None:
        pass


    def cal_distance(self, point1, point2):
        """Computes the Manhattan distance between two points"""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
