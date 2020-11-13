import pickle

import h5py
import numpy as np

from src.distance.distance_abstract import DistanceAbstract
from src.distance.distance_manhattan import ManhattanDistance


def main_obstacle_travel(xyxy, width, collapse):
    obstacle_traveler = ObstacleTraveler(ManhattanDistance().calc_manhattan, xyxy, width, collapse)
    obstacle_traveler = obstacle_traveler.new_distance_dict()
    return obstacle_traveler


class ObstacleTraveler:
    def __init__(self, distance_calculator=None, shelf_locations=None, width=None, collapse=None, distance_dict={}):
        self._calc_distance = distance_calculator
        self._shelf_locations = shelf_locations
        self._width = width
        self._collapse = collapse
        self._distance_dict = distance_dict


    @property
    def shelf_locations(self):
        return self._shelf_locations


    @property
    def distance_dict(self):
        return self._distance_dict


    @property
    def width(self):
        return self._width


    @property
    def collapse(self):
        return self._collapse


    @staticmethod
    def get_short_dir(manh):
        """
        :param manh: manh distance betw 2 points, each manh signifies directions distances (left and rightZZ)
        :return:
        """
        if manh[0] < manh[1]:
            return manh[0], -2
        else:
            return manh[1], 2


    @staticmethod
    def read_from_hdf5(name='obstacle_travel_distance', dataset_name='distnace_dict'):
        with h5py.File(name + 'hdf5', 'r') as f:
            data_set = f[dataset_name]
        return data_set


    @staticmethod
    def read_from_pickle(name='obstacle_travel_distance'):
        with open(name +'.pickle', 'rb') as pkl:
            res = pickle.load(pkl)
        return res


    def new_distance_dict(self):
        for (x1, y1), (x2, y2) in self._shelf_locations:
            if x1 == x2 and y1 == y2:
                """If two points are actually the same ones"""
                self.add_to_dict(1, 0, (x1, y1), (x2, y2))
                continue
            floor = x1 - self._width - self.collapse
            ceil = x1 + self._width + self.collapse
            x1_floor_ceil = np.array([floor, ceil])
            diff = x1_floor_ceil - x1
            x2_tmp = x2 - diff
            manh = np.array([
                self._calc_distance((x1_floor_ceil[0], y1), (x2_tmp[0], y2)),
                self._calc_distance((x1_floor_ceil[1], y1), (x2_tmp[1], y2))]).round(3)
            short_dir = self.get_short_dir(manh)
            self.add_to_dict(*short_dir, (x1, y1), (x2, y2))
        return self


    def add_to_dict(self, dist, left_or_right, xy1, xy2):
        xy1_key, xy2_key = "%s_%s" % (xy1[0], xy1[1]), "%s_%s" % (xy2[0], xy2[1])
        xy1_dict = {xy2_key: {'distance': dist, 'direction': left_or_right}}
        xy2_dict = {xy1_key: {'distance': dist, 'direction': left_or_right}}
        try:
            self._distance_dict[xy1_key].update(xy1_dict)
        except KeyError or TypeError:
            # insert new val, as no exists
            self._distance_dict.update({xy1_key: xy1_dict})
        try:
            self._distance_dict[xy2_key].update(xy2_dict)
        except KeyError or TypeError:
            # insert new val, as no exists
            self._distance_dict.update({xy2_key: xy2_dict})


    def save_to_hdf5(self, name='obstacle_travel_distance', dataset_name='distnace_dict'):
        with h5py.File(name + 'hdf5', "w") as f:
            f.create_dataset(dataset_name, data=self._distance_dict)


    def save_to_pickle(self, name='obstacle_travel_distance'):
        with open(name + ".pickle", "wb") as pkl:
            pickle.dump(self._distance_dict, pkl)


    def remove_shelf(self, xy):  # todo add later
        pass


    def add_shelf(self, xy):  # todo add later
        pass
