class Seat:
    def __init__(self, sector, number):
        self.sector = sector
        self.number = number
        self.status = False

    def __str__(self):
        return f"seat {self.number} in sector {self.sector}"

    def __repr__(self) -> str:
        return str(self)


class Stadium:
    def __init__(self, seats):
        self.seats = seats


stadium = Stadium([Seat(1, s) for s in range(1, 100+1)])


print(stadium.seats)
