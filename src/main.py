from Station import Station
from Charger import Charger
import sys

'''
Finding file
1. Traverse the file system to find the file
2. Open the file
'''

'''
Parsing the file/updating the Stations
1. Find the first expected header "[Station]" 
2. If that header is not "[Station]", raise some Error and exit
3. Get the ID of the station: id = ...
4. Create the station: station = Station(id) and add it to a dictionary of stations
5. modify the charger uptime based on the time series given
6. Update station uptime
7. Repeat for every charger in every station
8. Print the uptimes for each station
'''

Stations: dict[Charger] = {}


for id, station in Stations.items():
    print(f"{id} {station.get_uptime()}")
