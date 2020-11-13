import pickle

"""The file to add new stack/shelf - obstacle_travel_main.py"""

def read_from_pickle(name='obstacle_travel_distance'):
    path_to_pickle = 'obstacle_travel_distance.pickle'
    with open(path_to_pickle, 'rb') as pkl:
        res = pickle.load(pkl)
    return res

# 3.0_12.25
# 12.0_11.75


print(read_from_pickle())