def card_hide(card: str) -> str:
    hidden_card = '*' * len(card[0:-4])
    return ''.join(hidden_card + card[-4:])
