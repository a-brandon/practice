def find_all_digits(nums):
    nums = [str(num) for num in nums]
    check = [i for i in range(0, 10)]
    arr = []
    for i, elem in enumerate(nums):
        for num in elem:
            if int(num) not in arr:
                arr.append(int(num))
                arr = sorted(arr)
                if arr == check:
                    return int(nums[i])
    return 'Missing digits!'
