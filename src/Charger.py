class Charger:
    id: int
    times: list[tuple[int]]

    # Rounded down to the nearest percent
    uptime: int
    total_time: int

    def uptime():
        ...
    