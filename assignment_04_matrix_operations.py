# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0]) if rows else 0
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0]) if rows_a else 0
    cols_b = len(b[0]) if len(b) else 0
    product = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            sum_product = 0
            for k in range(cols_a):
                sum_product += a[i][k] * b[k][j]
            row.append(sum_product)
        product.append(row)
    return product

def print_matrix(matrix):
    if not matrix:
        print("Empty matrix")
        return
    col_widths = [max(len(str(matrix[i][j])) for i in range(len(matrix))) for j in range(len(matrix[0]))]
    for row in matrix:
        print(" ".join(str(val).rjust(col_widths[j]) for j, val in enumerate(row)))

def main():
    # Part A - Transpose a Matrix
    print("Part A - Transpose a Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print("Original Matrix:")
    print_matrix(matrix)
    print("Transposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    # Part B - Add Two Matrices
    print("\nPart B - Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter matrix A:")
    a = read_matrix(rows, cols)
    print("Enter matrix B:")
    b = read_matrix(rows, cols)
    print("Sum of matrices:")
    print_matrix(add_matrices(a, b))

    # Part C - Multiply Two Matrices
    print("\nPart C - Multiply Two Matrices")
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    if cols_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return
    print("Enter matrix A:")
    a = read_matrix(rows_a, cols_a)
    print("Enter matrix B:")
    b = read_matrix(rows_b, cols_b)
    print("Product of matrices:")
    print_matrix(multiply_matrices(a, b))

if __name__ == "__main__":
    main()
