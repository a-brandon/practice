s = 'ABABAB'
for i, _ in enumerate(s[:-2]): # Doing it this way we can check if the current element matches the letter two elements ahead of it, without exceeding index range.
  if s[i] != s[i + 2]: # Check if current element isn't equal to the element two index positions head.
    return False # Return False as soon as the condition isn't met

