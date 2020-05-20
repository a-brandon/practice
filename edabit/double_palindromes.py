def palindrome_set(lst):
    res = []
    
    for s in lst:
        count = 0
        digits = [d for d in s if d.isdigit()]
        letters = [c for c in s if c not in set(digits)]
        
        if digits == digits[::-1] and digits:
            count += 1
        if letters == letters[::-1] and letters:
            count += 1
            
        res.append(count)
        
    return res
