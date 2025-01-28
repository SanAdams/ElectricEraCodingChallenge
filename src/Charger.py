from math import floor

class Charger:

    def __init__(self, id: int, last_time: int):
        self.id = id
        self.time_up = 0
        self.total_time = 0
        self.uptime = 0
        self.last_time = last_time

    def get_uptime(self):
        return self.uptime

    def update_uptime(self, times: tuple[int], up: bool) -> int:

        # Capture gaps in time
        gap_time = times[1] - self.last_time

        delta_time = times[1] - times[0]
        if up:
            self.time_up += delta_time
        
        self.total_time += (delta_time + gap_time)
        self.uptime = floor((self.time_up / self.total_time) * 100)

    

    