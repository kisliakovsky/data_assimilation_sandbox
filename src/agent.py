from src.location import Location


class Agent(object):

    def __init__(self):
        self.__head_direction = 90.0
        self.__location = Location(4.0, 5.0)
        self.__destination = Location(13.0, 11.0)

    @property
    def head_direction(self) -> float:
        return self.__head_direction

    @property
    def location(self) -> Location:
        return self.__location

    destination = property()

    @destination.getter
    def destination(self) -> Location:
        return self.__destination

    @destination.setter
    def destination(self, new_destination: Location):
        self.__destination = new_destination
