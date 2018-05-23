"Function that returns values from a set using specific set of distribution"
from numpy import random, linspace

def Fixed(val):
  "Return a fixed selected value"
  return val

def Boolean():
    "Return a random bool"
    return random.choice([True, False])

def Choice(selection):
    """Return a random value from an explicit list of choice.
    Args:
        *selection: a set of explicit choices
    Returns:
        an element of the selecting
    """
    x = random.choice(selection)
    if isinstance(selection[0], int):
        return int(x)
    elif isinstance(selection[0], float):
        return float(x)
    elif isinstance(selection[0], str):
        return str(x)
    else:
        Exception('unknown type')

def Range(start, stop, increment):
    """Return a random value from a range.
    Args:
        start (int): lower bound of the range
        stop (int): upper bound of the range
        increment (int): incremental step
    Returns:
        an element of the range
    
    Todo:
      Don't generate the full range, do something more optimal
    """
    my_range = range(start, stop, increment)
    return int(random.choice(my_range))

def Linear(start, stop, num_buckets, precision):
    """Return a random value from a range which is linearly divided.
    Args:
        start (int/float): lower bound of the range
        stop (int/float): upper bound of the range
        divider (int): into how many buckets should the range being divided in
        precision (int): For float range. Round the result rounded to the nth decimal if needed. 0 means not rounded
    Returns:
        an element of the range
    
    Todo:
      Don't generate the full range, do something more optimal
    """
    my_range = linspace(start, stop, num_buckets)
    var = random.choice(my_range)
    if isinstance(start, int):
        return int(var)
    else:
        var = float(var)
        if precision > 0:
            var = round(var, precision + 1)
        return var

if __name__ == "__main__":
    x = Choice(1, 2, 3)
    print(isinstance(x, int))
    print(type(x))

    x = Choice(1.1, 2.2)
    print(isinstance(x, float))
    print(type(x))