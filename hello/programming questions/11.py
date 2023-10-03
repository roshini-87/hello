def fourSum(nums, target):
    nums.sort()
    result = set()  
    pair_sums = {}

    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            pair_sum = nums[i] + nums[j]
            if pair_sum in pair_sums:
                pair_sums[pair_sum].append((i, j))
            else:
                pair_sums[pair_sum] = [(i, j)]

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            remaining_sum = target - nums[i] - nums[j]

            if remaining_sum in pair_sums:
                for pair in pair_sums[remaining_sum]:
                    if pair[0] > j:
                        result.add((nums[i], nums[j], nums[pair[0]], nums[pair[1]]))

    return list(result)

S = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(S, target)

for quadruplet in result:
    print(quadruplet)
