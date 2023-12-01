from abc import ABC, abstractmethod

class RouteStrategy(ABC):
    @abstractmethod
    def calculate_route(self, start_point: str, end_point: str) -> str:
        pass

class FastestRoute(RouteStrategy):
    def calculate_route(self, start_point: str, end_point: str) -> str:
        return f"Fastest route from {start_point} to {end_point}"

class ShortestRoute(RouteStrategy):
    def calculate_route(self, start_point: str, end_point: str) -> str:
        return f"Shortest route from {start_point} to {end_point}"

class ScenicRoute(RouteStrategy):
    def calculate_route(self, start_point: str, end_point: str) -> str:
        return f"Scenic route from {start_point} to {end_point}"
class MapApp:
    def __init__(self, route_strategy: RouteStrategy):
        self.route_strategy = route_strategy

    def set_route_strategy(self, route_strategy: RouteStrategy):
        self.route_strategy = route_strategy

    def calculate_route(self, start_point: str, end_point: str) -> str:
        return self.route_strategy.calculate_route(start_point, end_point)

map_app = MapApp(FastestRoute())
print(map_app.calculate_route("Home", "Office"))  # Uses FastestRoute

map_app.set_route_strategy(ScenicRoute())
print(map_app.calculate_route("Home", "Office"))  # Uses ScenicRoute
