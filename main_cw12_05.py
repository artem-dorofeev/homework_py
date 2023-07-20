class Hotel:
    def __init__(self, value, rooms = 255):
        self.__name = None
        self._name = value
        # self.rooms = rooms

    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self.__name = value


hotel = Hotel("ZP")


