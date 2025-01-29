from Charger import Charger

class Station:

    def __init__(self, id: int):
        self.id = id
        self.uptime = 0
        self.Chargers: list[Charger] = [] 
        
    def update_uptime(self):
        ...

    def add_charger(self, charger: Charger):
        self.Chargers.append(charger)