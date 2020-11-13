from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver.routing_enums_pb2  import FirstSolutionStrategy
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
        10,
        maximum_distance,
        True,
        distance)
    distance_dimension = routing.GetDimensionOrDie(distance)
    distance_dimension.SetGlobalSpanCostCoefficient(0)



def main(num_carts, locations, pre_calced_distances):
    """Entry point of the program"""
    # Instantiate the data problem.
    print(">>> num_carts", num_carts)
    print(">>> locations", locations)
    print(">>> pre_calced_distances", pre_calced_distances)
    data = DataProblem(num_carts, locations)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(data.num_locations, data.num_carts, data.depot)

    distance_evaluator = CreateDistanceEvaluator(data, pre_calced_distances).distance_evaluator
    routing.SetArcCostEvaluatorOfAllVehicles(distance_evaluator)
    add_distance_dimension(routing, distance_evaluator)

    # Setting first solution heuristic (cheapest addition).
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        printer = ConsolePrinter(data, routing, assignment, distance_evaluator)
        response = printer.print()
    return response
