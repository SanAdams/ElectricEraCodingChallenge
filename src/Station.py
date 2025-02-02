from Charger import Charger
from math import floor

class Station:

    def __init__(self, id: int):
        self.id = id
        self.uptime = 0
        self.Chargers: dict[Charger] = {}

        # Probability that all chargers are down
        self.downtime_product = 1.0
        
    def update_uptime(self, old_uptime: float, new_uptime: float):

        old_downtime = (100 - old_uptime) / 100
        new_downtime = (100 - new_uptime) / 100
        self.downtime_product = self.downtime_product / old_downtime * new_downtime
        self.uptime = floor((100 * (1 - self.downtime_product)))

    def add_charger(self, charger: Charger):
        self.Chargers[charger.id] = charger
    
    def get_uptime(self):
        return self.uptime
        