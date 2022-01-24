def direction(facing, turn):
    """
    This function receive the direction you are facing
    (one of the 8 directions: N, NE, E, SE, S, SW, W, NW)
    and a certain degree to turn (a multiple of 45, between -1080 and 1080).
    Return the direction you will face after the turn.

    :param facing: direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW)
    :type facing: str
    :param turn: certain degree to turn (a multiple of 45, between -1080 and 1080)
    :type turn: int
    """
    sides_degrees = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315
    }
    degrees_sides = {
        0: "N",
        45: "NE",
        90: "E",
        135: "SE",
        180: "S",
        225: "SW",
        270: "W",
        315: "NW",
        360: "N"
    }

    if not isinstance(facing, str):
        raise TypeError('type of the first argument should be "str"')

    try:
        sides_degrees[facing]
    except KeyError:
        raise ValueError('incorrect value of the first argument') from None

    if not isinstance(turn, int):
        raise TypeError('type of the second argument should be "int"')

    if not -1080 <= turn <= 1080:
        raise ValueError('second argument should be between -1080 and 1080')

    if bool(turn % 45):
        raise ValueError('second argument should be multiple of 45')

    new_position = (sides_degrees[facing] + turn) % 360
    return degrees_sides[new_position]
