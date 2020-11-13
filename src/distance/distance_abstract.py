from abc import ABC, abstractmethod


class DistanceAbstract(ABC):

    @abstractmethod
    def cal_distance(self, point1, point2):
        """Computes the distance between two points"""
        pass

    @staticmethod
    @abstractmethod
    def distance_calculator(self, point1, point2):
        """Computes the distance between two points"""
        pass


    @staticmethod
    @abstractmethod
    def manhattan(point1, point2):
        pass
