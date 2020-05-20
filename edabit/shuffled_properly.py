def is_shuffled_well(nums):
    curr_num, count = nums[0], 1

    for n in nums[1:]:
        if n + 1 == curr_num or n - 1 == curr_num:
            count += 1
        else:
            count = 1

        if count == 3:
            return False

        curr_num = n

    return True
