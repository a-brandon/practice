def molar_mass(compound):
    elems = {'Water': 'H2 O',
             'BoricAcid': 'H3 B O3',
             'SulfuricAcid': 'H2 S O4',
             'NitricAcid': 'H N O3',
             'HydroChloricAcid': 'H Cl'}
    nums = {'H': 1,
            'B': 10,
            'O': 16,
            'S': 32,
            'N': 14,
            'Cl': 35}
    return sum(nums[e] if e in nums else nums[e[0]] * int(e[-1]) for e in elems[compound].split())