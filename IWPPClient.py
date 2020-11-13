from IWPPExecutor import IWPPExecutor
from modules.kinetic_core.AbstractClient import AbstractClient, rpc
from modules.kinetic_core.AbstractExecutor import executor


@executor(IWPPExecutor)
class IWPPClient(AbstractClient):
    @rpc
    async def get_cart_route(self, data):
        """
        :param data:{
            'num_carts': 2, # num of carts/pickers available
            'locations': [(x1,y1), (x2,y2), ...] # x and y locations of each picking point
        }
        :return: optimized sequence of nodes to be visited {
            # todo final structure to be done
        }
        """
        pass


    @rpc
    async def get_distance(self, points):
        """
        :param points: two points to calculate the distance between them {
            point1: (x1,y1),
            point2: (x2, y2)
        }
        :return: distance
        """
        pass


    @rpc
    async def get_pre_calculated_distances(self):
        """
        :return: all pre-calculated points between shelves and/or picking point
        """
        pass


    @rpc
    async def recalculate_distances(self, configs):
        """
        :param configs: params of the new warehouse distance points {
            x: 10, # max_x point,
            x_steps: 0.5, # cross-roads every x-steps
            y: 10, # max_y point,
            y_steps: 0.5, # cross-roads every y-steps
        }
        :return: all pre-calculated points between shelves and/or picking point
        """
        pass
