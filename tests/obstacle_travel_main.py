import sys
# sys.path.append('../')
from itertools import product
import numpy as np
from src.distance.obstacle_travel import main_obstacle_travel

"""The file to add new stack/shelf"""


x = np.arange(2.85, 5.21+0.01, step=2.36).round(2)
y = np.arange(1.56, 15.00+.01, step=1.68).round(2).tolist()

xy = list(product(x, y))
xy = xy + [(4.21, 0.25), (8.56, 7.57), (5.21, 17)]
xyxy = list(product(xy, xy))
width = 2.7 / 2
collapse = 1 / 2

if __name__ == '__main__':
    pass
    obstacle_traveler = main_obstacle_travel(xyxy, width, collapse)
    obstacle_traveler.save_to_pickle()
    print(obstacle_traveler._distance_dict)
