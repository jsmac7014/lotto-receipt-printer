import random
from typing import List


def generate_line() -> List[int]:
    """Generate one line of 6 unique numbers from 1 to 45, sorted ascending."""
    return sorted(random.sample(range(1, 46), 6))


def generate_lines(count: int = 1) -> List[List[int]]:
    """Generate multiple lines."""
    return [generate_line() for _ in range(count)]
