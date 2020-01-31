from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for elem in elements:
        if elem != elements[0]:
            return False
    return True
