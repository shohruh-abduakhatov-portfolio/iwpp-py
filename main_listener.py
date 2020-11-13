import asyncio
import logging

from IWPPExecutor import IWPPExecutor
from modules.kinetic_core import Logger
from modules.kinetic_core.AbstractExecutor import executor
from modules.kinetic_core.QueueListener import QueueListener
from src.distance.obstacle_travel import ObstacleTraveler


main_loop = asyncio.get_event_loop()

Logger.init(level=logging.DEBUG)

# Регистрируем наш слушатель - он принимает сообщения из очереди rabbitMQ

distances_dict = ObstacleTraveler().read_from_pickle('src/distance/obstacle_travel_distance')


@executor(IWPPExecutor)
class IWPPExecutorListener(QueueListener):
    async def parse(self, task):
        print('[###] IWPP > start')
        await IWPPExecutor(task, distance=distances_dict).parse()


main_loop.create_task(IWPPExecutorListener().register_listener(main_loop))
main_loop.run_forever()
