import pdb
def two_sum(nums, target):
    # Create a dictionary to store the difference (target - num) and its index
    num_dict = {}

    n = len(nums)

    for i in range(n):
        # Calculate the complement
        complement = target - nums[i]
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Otherwise, store the current number with its index
        num_dict[nums[i]] = i

    return None  # Return None if no pair is found

# Example usage
nums = [2, 7, 11, 15]
target = 17
result = two_sum(nums, target)
print("Indices of the pair:", result)  # Output: [0, 3]
