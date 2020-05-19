def closest_palindrome(num):
    low = num - 1
    
    while str(num) != str(num)[::-1]:
        if str(low) == str(low)[::-1] and str(num) == str(num)[::-1]:
            return low
        elif str(low) == str(low)[::-1]:
            return low

        low -= 1
        num += 1
        
    return num
