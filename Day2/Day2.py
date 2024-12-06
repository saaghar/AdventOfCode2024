import fileinput

# Function to make list of rows from input file
def make_lists():
    _list = []
    for line in fileinput.input(files='dataDay2.txt'):
        row = list(map(int, line.strip().split()))
        _list.append(row)
    return _list

# Function to check line safety
def check_line_safety():
    rows = make_lists()  # Get the list of rows from input file
    safe = []  # List to store safe rows
    unsafe = []  # List to store unsafe rows

    for idx, row in enumerate(rows):
        # Check if the row is strictly increasing or strictly decreasing
        is_increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
        is_decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))
        
        # Check if each adjacent element differs by at least 1 and at most 3
        is_safe_difference = all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))
        
        # Determine if the row is safe or unsafe
        if (is_increasing or is_decreasing) and is_safe_difference:
            safe.append(f"Line {idx + 1}: safe")
        else:
            unsafe.append(f"Line {idx + 1}: unsafe")
    
    return safe, unsafe

# Call the function and print the results
safe_results, unsafe_results = check_line_safety()

print("Safe Lines:")
for result in safe_results:
    print(result)
print(f"Total Safe Lines: {len(safe_results)}")

#print("\nUnsafe Lines:")
#for result in unsafe_results:
#    print(result)
#print(f"Total Unsafe Lines: {len(unsafe_results)}")
