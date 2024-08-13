import time
from math import factorial

def permutations(n):
    nums = list(range(1, n + 1))  # Generate list of first n natural numbers
    result = []
    
    def backtrack(start):
        if start == n:
            result.append(nums[:])  # Make a copy of current permutation
            print(nums)  # Print the current permutation
        else:
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack
    
    backtrack(0)
    return result

# Get input from user for n
n = int(input("Enter a number (n) to generate permutations of first n natural numbers: "))

# Example usage with timestamps
print(f"Generating permutations of first {n} natural numbers...")
start_time = time.time()

perms = permutations(n)

end_time = time.time()
print(f"Generated {len(perms)} permutations in {end_time - start_time:.6f} seconds.")
