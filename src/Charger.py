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

    def update_uptime(self, times: tuple[int], up: bool):
        start, end = times

        if start > end: 
            raise ValueError("ERROR")
        elif end < self.last_time:
            raise ValueError("ERROR")
        
        # Capture gaps in time
        gap_time = end - self.last_time

        delta_time = end - start
        if up:
            self.time_up += delta_time
        
        self.total_time += (delta_time + gap_time)
        self.uptime = floor((self.time_up / self.total_time) * 100)

    

    