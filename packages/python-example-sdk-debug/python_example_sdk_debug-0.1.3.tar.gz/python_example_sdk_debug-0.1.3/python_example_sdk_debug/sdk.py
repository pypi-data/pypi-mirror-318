
from random_lib_debug import generate_random_int

def add(a: int, b: int) -> int:
    return a + b

def addAndRandomize(a: int, b: int, min_rand: int, max_rand: int) -> int:
    """
    Add two integers and add a random integer between min_rand and max_rand.
    
    :param a: First integer.
    :param b: Second integer.
    :param min_rand: Minimum value for random integer.
    :param max_rand: Maximum value for random integer.
    :return: The sum of a, b, and a random integer.
    """
    random_int = generate_random_int(min_rand, max_rand)
    print(f"Random integer: {random_int}")
    return a + b + random_int