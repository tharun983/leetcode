def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]

        # If not found, add the current number and its index to the dictionary
        num_indices[num] = i

    # If no solution is found
    return None

