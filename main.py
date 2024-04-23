from datetime import datetime, timedelta
import database as db
import concurrent.futures as cf
from airlines.ryan import add_daily_oneways, ryanair

# Dijkstra algorithm test imports
from airlines.ryan import airports
from ryanair import Ryanair
from ryanair.types import Flight
from misc.dijkstra import find_path


def main():
    # add_daily_oneways(6)
    # add_daily_oneways(7)

    # Dijkstra algorithm testing
    # ryanair = Ryanair("EUR")
    # data: list[Flight] = []
    # start = datetime.today().date() + timedelta(days=1)
    # for code in airports:
    #     f = ryanair.get_cheapest_flights(code, start, start + timedelta(days=1))
    #     data.extend(f)

    data = db.all_ryanair_oneways()
    find_path(data)

    # rows = db.all_ryanair_oneways()
    # print(rows)


if __name__ == "__main__":
    main()
