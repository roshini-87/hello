def generate_pascals_triangle(numRows):
    triangle = []
    for row in range(numRows):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                # Sum of the two values from the previous row
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(value)
        triangle.append(current_row)
    return triangle

# Example usage:
numRows = 5
result = generate_pascals_triangle(numRows)

# Print the result
for row in result:
    print(row)
