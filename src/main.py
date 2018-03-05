import numpy

random_state = numpy.random.RandomState(47)


class Location(object):

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return '({};{})'.format(self.__x, self.__y)


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


def perform_gaussian_process(w: float, t: float):
    variance = 1.0
    d = 6
    d_new = -1
    while d_new <= 0:
        d_new = round(variance * random_state.randn() + d)
    return d_new


def generate_new_destination(agent: Agent) -> Location:
    head_direction = agent.head_direction
    location = agent.location
    d_new = perform_gaussian_process(3.0, 5.0)
    return Location(0.0, 0.0)


def main():
    destination = generate_new_destination(Agent())


if __name__ == '__main__':
    main()
