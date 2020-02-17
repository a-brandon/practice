def make_sandwich(i: list[str], f: str) -> list:
    """Makes a sandwich.
    
    Creates a sandwich based off the ingredients in the list.
    If the ingredient == f, then "bread" gets placed around the ingredient.
    
    Parameters:
        i: Ingredients
        f: An ingredient to place "bread" around.
    Returns:
        A sandwich."""
    sandwich = ''
    for ingredient in i:
        if ingredient == f:
            sandwich += 'bread ' + f + ' bread '
        else:
            sandwich += ingredient + ' '
    return sandwich.split()
