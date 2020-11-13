from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver.routing_enums_pb2 import FirstSolutionStrategy
from ortools.constraint_solver import routing_enums_pb2

from src.console_printer import ConsolePrinter
from src.distance.distance_manhattan import ManhattanDistance
from src.evals import *
from src.models.data_problem import DataProblem


def add_distance_dimension(routing, distance_evaluator):
    """Add Global Span constraint"""
    distance = 'Distance'
    maximum_distance = 30000  # Maximum distance per vehicle.
    routing.AddDimension(
        distance_evaluator,
        0,
        maximum_distance,
        True,
        distance)
    distance_dimension = routing.GetDimensionOrDie(distance)
    distance_dimension.SetGlobalSpanCostCoefficient(100)


def main(num_carts, locations, pre_calced_distances):
    """Entry point of the program"""
    # Instantiate the data problem.

    data = DataProblem(num_carts, locations)
    dist_callback = CreateDistanceEvaluator(data, pre_calced_distances).distance_evaluator
    tsp_size = len(locations)
    num_routes = 1
    depot = 0

    # Create routing model.
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        print(assignment)
        if assignment:
            # Solution cost.
            print("Total distance: " + str(assignment.ObjectiveValue()) + "\n")
            # Inspect solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1.
            route_number = 0
            node = routing.Start(route_number)
            start_node = node
            route = ''

            while not routing.IsEnd(node):
                route += str(node) + ' -> '
                node = assignment.Value(routing.NextVar(node))
            route += '0'
            print("Route:\n\n" + route)
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


