# These are the basic left and right binary search function for the insert positions
def binary_left(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l

def binary_right(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
    return l

# Now, some basic tests
nums = [0, 1, 2, 2, 3, 3, 4, 5, 7, 8, 9]
for i, n in enumerate(nums):
    print('{}[{}] '.format(i, n), end='')


targets = [0, 1, 2, 3, 5, 9, 10, -1]
print('\n binary left insert pos search:')
for target in targets:
    print("{}[{}] ".format(target, binary_left(nums, target)), end='')


print('\n binary right insert pos search:')
for target in targets:
    print("{}[{}] ".format(target, binary_right(nums, target)), end='')

print('\n number count:')
for target in targets:
    print("{}[{}] ".format(target, binary_right(nums, target) - binary_left(nums, target)), end='')
