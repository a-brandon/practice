def build_profile(*args, **kwargs):
    return dict(zip(['first_name', 'last_name'], args), **kwargs)
