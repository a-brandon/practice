def get_order(order: str) -> str:
    """Cleans up a menu.
    
    Based on a menu, returns a cleaned up string from the string
    with spaces & shifts.
    
    Args:
        order: A string
    
    Returns:
        A string
    """
    food_list = ['burger', 'fries', 'chicken', 'pizza', 'sandwich',
                 'onionrings', 'milkshake', 'coke']
    output = ''
    menu = []
    for ch in order:
        output += ch
        if output in food_list:
            menu.append(output)
            output = ''
    cleaned_menu = ' '.join(sorted(menu, key=lambda x: food_list.index(x))).title()
    return cleaned_menu
