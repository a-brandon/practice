def award_prizes(names):
    ranks = sorted(names.values(), reverse=True)[:3]
    awards = ['Gold', 'Silver', 'Bronze']
    return {k: awards[ranks.index(v)] if v in ranks else 'Participation' for k, v in names.items()}