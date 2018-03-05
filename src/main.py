import numpy

from src.agent import Agent
from src.location import Location

gaussian_generator = numpy.random.RandomState(47)
direction_generator = numpy.random.RandomState(37)
num_of_directions_generator = numpy.random.RandomState(71)
opposite_direction_generator = numpy.random.RandomState(59)
location_x_generator = numpy.random.RandomState(89)
location_y_generator = numpy.random.RandomState(113)


def perform_gaussian_process(w: float, t: float):
    variance = 1.0
    d = 6
    d_new = -1
    while d_new <= 0:
        d_new = round(variance * gaussian_generator.randn() + d)
    return d_new


def select_new_head_direction_and_location(head_direction: float, location: Location):
    num_of_directions = num_of_directions_generator.randint(1, 5)
    p = 0.2
    q = (1 - p) / num_of_directions
    probabilities = [p] + [q for _ in range(num_of_directions)]
    opposite_direction = head_direction + 180
    if opposite_direction >= 360.0:
        opposite_direction -= 360.0
    directions = [opposite_direction] + [direction_generator.uniform(0.0, 360.0) for _ in range(num_of_directions)]
    index = opposite_direction_generator.multinomial(1, probabilities).tolist().index(1)
    new_head_direction = directions[index]
    new_location = Location(location.x + numpy.sin(numpy.deg2rad(new_head_direction)),
                            location.y + numpy.cos(numpy.deg2rad(new_head_direction)))
    return new_head_direction, new_location


def generate_new_destination(agent: Agent) -> Location:
    head_direction = agent.head_direction
    location = agent.location
    d_new = perform_gaussian_process(3.0, 5.0)
    for i in range(d_new):
        head_direction, location = select_new_head_direction_and_location(head_direction, location)
    nearest_location = Location(location.x - 1, location.y - 1)
    x = location_x_generator.uniform(nearest_location.x, location.x)
    y = location_y_generator.uniform(nearest_location.y, location.y)
    return Location(x, y)


def main():
    destination = generate_new_destination(Agent())
    print(destination)


if __name__ == '__main__':
    main()
