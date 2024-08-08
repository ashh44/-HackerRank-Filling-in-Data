def construct_pyramid(a):
    pyramid = []
    index = 0
    row_length = 1
    
    while index < len(a):
        pyramid.append(a[index:index + row_length])
        index += row_length
        row_length += 1
        
    return pyramid

def maximum_path(a):
    if not a:
        return 0

    pyramid = construct_pyramid(a)
    
    # Start from the second last row and move upwards to the top
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            # Update the value of each element to be the sum of itself and the max of the two elements directly below it
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
    
    # The top element contains the maximum path sum
    return pyramid[0][0]

# Example usage
a = [1, 3, -1, 3, 1, 5]
print(maximum_path(a))  # Output should be 7