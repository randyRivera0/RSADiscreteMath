def print_power_set(n):
    # Generate the input set {1, 2, ..., n}
    input_set = list(range(1, n + 1))
    
    # Get the length of the input set
    n = len(input_set)
    
    # There are 2^n subsets
    power_set_size = 2 ** n
    
    # Generate each subset
    for i in range(power_set_size):
        subset = []
        for j in range(n):
            # Check if the jth element is in the ith subset
            if i & (1 << j):
                subset.append(input_set[j])
        print(subset)

# Example usage
n = int(input("Set cardinality: "))
print_power_set(n)
