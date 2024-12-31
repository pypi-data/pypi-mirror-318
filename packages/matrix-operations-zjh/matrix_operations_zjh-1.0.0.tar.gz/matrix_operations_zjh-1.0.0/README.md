# Matrix_Operations_zjh

A simple Python package for matrix operations including addition and multiplication.
this package is used for homework with little change
## Installation

```
sh
pip install matrix_operations
```
## Usage

```
python
from matrix_operations import add_matrices, multiply_matrices

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Add matrices
result_add = add_matrices(matrix1, matrix2)
print(result_add)  # Output: [[6, 8], [10, 12]]

# Multiply matrices
result_multiply = multiply_matrices(matrix1, matrix2)
print(result_multiply)  # Output: [[19, 22], [43, 50]]
