def get_name_and_top_note(students):
    return [{'name': x['name'], 'top_note': max(x['notes']) if x['notes']else 0} for x in students]