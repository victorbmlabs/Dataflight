from ryanair import Ryanair
from ryanair.types import Flight
from datetime import datetime, timedelta
from dotenv import load_dotenv
import database as db

ryanair = Ryanair("EUR")

with open("airlines/iata_codes_ryanair.txt") as f:
    airports = f.read().split(",")


def add_daily_oneways(delta: int = 1):
    start = datetime.today().date() + timedelta(days=delta)
    data: list[Flight] = []
    for code in airports:
        f = ryanair.get_cheapest_flights(code, start, start + timedelta(days=1))
        data.extend(f)

    print(f"Adding {len(data)} flights to database")
    db.add_ryanair_oneways(data)
