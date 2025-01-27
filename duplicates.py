
def containsDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False

if __name__ == "__main__":
    array = [1,2,3,1]
    containsDuplicate(array)