import heapq
import datetime
from ryanair.types import Flight


def dijkstra_with_constraints(
    start, end, flights: list[Flight], max_stops, max_price, max_days_between
):
    heap = [(0, start, 0, [])]  # (total price, current airport, stops, path)
    visited = set()

    while heap:
        total_price, current, stops, path = heapq.heappop(heap)

        if current == end:
            return total_price, path

        if current in visited:
            continue
        visited.add(current)

        for flight in flights:
            if flight.origin == current:
                if stops + 1 <= max_stops and total_price + flight.price <= max_price:
                    # Calculate days between flights
                    if not path:
                        days_between = 0
                    else:
                        days_between = (
                            flight.departure_time - path[-1].departure_time
                        ).days

                    if days_between <= max_days_between:
                        heapq.heappush(
                            heap,
                            (
                                total_price + flight.price,
                                flight.destination,
                                stops + 1,
                                path + [flight],
                            ),
                        )

    return float("inf"), None


def find_path(flights: list[Flight]):
    start_airport = "ZAD"  # Tirana
    end_airport = "EIN"  # Bari

    max_stops = 3
    max_price = 110  # Set your maximum price
    max_days_between = 2  # Set your maximum days between flights

    total_price, path = dijkstra_with_constraints(
        start_airport, end_airport, flights, max_stops, max_price, max_days_between
    )

    if path:
        print("Optimal path found:")
        for flight in path:
            print(
                f"From {flight.origin} to {flight.destination} at {flight.departure_time}, price: {flight.price}"
            )
        print(f"Total price: {total_price}")
    else:
        print("No path found within constraints.")
