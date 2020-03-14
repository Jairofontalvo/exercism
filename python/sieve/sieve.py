def primes(limit):
    nums = list(range(2, limit + 1))
    for i in nums:
        for multiple in range(2, len(nums)):
            product = i * multiple
            if product > max(nums):
                break
            elif product in nums:
                nums.remove(product)
    return nums
