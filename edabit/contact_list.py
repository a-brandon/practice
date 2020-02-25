def sort_contacts(names, sort):
    if names is None:
        return []
    if len(names) == 1:
        return names
    if sort == 'ASC':
        return sorted(names, key=lambda x: x.split()[-1])
    return sorted(names, key=lambda x: x.split()[-1], reverse=True)
