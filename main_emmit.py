import asyncio
import logging

from IWPPClient import IWPPClient
from modules.kinetic_core import Logger


main_loop = asyncio.get_event_loop()

Logger.init(level=logging.DEBUG)


async def get_cart_route():
    iwpp_exec = IWPPClient(main_loop)
    print(">>>get_cart_route: Start")
    locations = [(3.0, 0.75), (3.0, 3.25)]
    num_carts = 2
    data = {
        'locations': locations,
        'num_carts': num_carts
    }

    iwpp = await iwpp_exec.get_cart_route(data=data)
    print(">>> get_cart_route: Result received")
    print(iwpp)
    return iwpp


async def get_distance():
    iwpp_exec = IWPPClient(main_loop)
    print(">>>get_distance: Start")
    iwpp = await iwpp_exec.get_distance(points={'point1': (3.0, 0.75), 'point2': (3.0, 3.25)})
    print(">>> get_distance: Result received")
    print(iwpp)


async def get_pre_calculated_distances():
    iwpp_exec = IWPPClient(main_loop)
    print(">>>get_pre_calculated_distances: Start")
    iwpp = await iwpp_exec.get_pre_calculated_distances()
    print(">>> get_pre_calculated_distances: Result received")
    print(iwpp)


async def recalculate_distances():
    iwpp_exec = IWPPClient(main_loop)
    print(">>>recalculate_distances: Start")
    iwpp = await iwpp_exec.recalculate_distances(configs={})
    print(">>> recalculate_distances: Result received")
    print(iwpp)


# main_loop.create_task(get_cart_route())
main_loop.create_task(get_distance())
# main_loop.create_task(get_pre_calculated_distances())
# main_loop.create_task(recalculate_distances())
main_loop.run_forever()
