from itertools import product

import numpy as np

from modules.kinetic_core.AbstractExecutor import AbstractExecutor
from src.distance.obstacle_travel import main_obstacle_travel
from src.in_warehouse_product_picker import main


class IWPPExecutor(AbstractExecutor):

    def __init__(self, task, distance):
        super().__init__(task)
        self.distance = distance


    # def __init__(self, task, distances):
    #
    #     # super().__init__(self, task)
    #     self.distance = distances



    async def get_cart_route(self, data):
        num_carts = data['num_carts']
        locations = data['locations']
        res = main(num_carts, locations, self.distance)
        return res


    async def get_distance(self, points):
        key_format = "%s_%s"
        key1 = key_format % (points['point1'][0], points['point1'][1])
        key2 = key_format % (points['point2'][0], points['point2'][1])
        try:
            res = self.distance[key1][key2]
        except KeyError:
            return "No such locations %s" % points
        return res


    async def get_pre_calculated_distances(self):
        return self.distance


    async def recalculate_distances(self, configs):
        x = np.arange(0, configs['x'], step=configs['x_steps']).round(3)
        x = list(filter(lambda x: not x.is_integer() or x == 0., x))
        y = np.arange(0, configs['y'], step=configs['y_steps']).tolist()
        xy = list(product(x, y))
        xyxy = list(product(xy, xy))
        width = configs['width'] / 2
        collapse = configs['collapse'] / 2
        obstacle_travel = main_obstacle_travel(xyxy, width, collapse)
        obstacle_travel.save_to_pickle()
        print("New Warehouse structure saved!")
        print(obstacle_travel._distance_dict)
        return "Please restart IWPP listener!"


