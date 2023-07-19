import pickle
from collections import 


class Hotel:
    def __init__(self, rooms) -> None:
        self.rooms = rooms

continental = Hotel(250)


with open("hotel.bin", "wb") as f:
    pickle.dump(continental, f)


