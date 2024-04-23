from datetime import datetime, timedelta
from ryanair import Ryanair
from ryanair.types import Flight
import ryanair.airport_utils as ap_utils
import csv
import database as db
import asyncio
from typing import List

api = Ryanair("EUR")
flights = []
coroutine_pool = []
start = datetime.today().date() + timedelta(days=1)

async def get_flights_async(from_iata: str, to_iata: str, start: datetime) -> List[Flight]:
    return await api.get_cheapest_flights(from_iata, to_iata, start, start+timedelta(days=1))
    
async def main():
    with open("iata_codes.txt") as f:
        airports = f.read().split(",")

    for code in airports:
        coroutine = get_flights_async(api, code, start)
        coroutine_pool.append(coroutine)

    print("Executing coroutine pool")
    results = await asyncio.gather(*coroutine_pool)

    flattened_flights = [flight.data_dict() for result in results for flight in result]

    print("Adding flights to database")
    db.add_ryanair_flights(flattened_flights)

asyncio.run(main())