#write a program to print matrix containing a group of similar elements by givin the input randomly in another matrix.
#write a program to print a matrix along with summtion of row elements and clumn elements after entering a 3*3 matrix.
#write a program to print the transpose of a matrix n*n order.
#write a program to check if a value is present in list or not using lambda function.
#write a program to print fibonacci series upto n terms using lambda.


def is_valid(matrix, visited, row, col, target):
    rows = len(matrix)
    cols = len(matrix[0])
    return (row >= 0 and row < rows and col >= 0 and col < cols and 
            not visited[row][col] and matrix[row][col] == target)

def dfs(matrix, visited, row, col, target, group):
    row_nbr = [-1, 0, 0, 1]
    col_nbr = [0, -1, 1, 0]

    visited[row][col] = True
    group.append((row, col))

    for k in range(4):
        if is_valid(matrix, visited, row + row_nbr[k], col + col_nbr[k], target):
            dfs(matrix, visited, row + row_nbr[k], col + col_nbr[k], target, group)

def print_groups(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    groups = []

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                group = []
                dfs(matrix, visited, i, j, matrix[i][j], group)
                groups.append(group)

    for group in groups:
        print("Group:", group)

# Example usage
matrix = [
    [1, 1, 2, 3],
    [3, 2, 2, 2],
    [4, 4, 4, 4],
    [5, 5, 5, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nGroups of Similar Elements:")
print_groups(matrix)
