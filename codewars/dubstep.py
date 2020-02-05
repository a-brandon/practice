def song_decoder(song: str) -> str:
    """
    Decodes a song.

    Removes 'WUB' from the given string, and returns the decoded string.

    Args:
        song: A string.

    Returns:
        A decoded string.
    """
    return ' '.join(song.replace('WUB', ' ').lstrip().split())
