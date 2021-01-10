## Matrix Math
Providing simple Matrix functionalities such as multiplication

## Disclaimer
*Just Multiplication implemented!* Unlikely that it gets further developed. It just serves as a first simple try on writing own python packages

*Due to using float values the resulting values can have a small deviation*
In a real project numpy would be used. This is just a training repository.

## Purpose
This repository serves as a training project for the author with python packages

## How to use
```python
from matrixmath import Matrix, EvenMatrix, Multiplication
matrix1 = Matrix (23, 24, -109) # 23 rows, 24 columns initialized with -109
matrix2 = EvenMatrix (3, 13) # 3 rows, 3 colums, initialized with 13
Multiplication().operate(matrix1, matrix2) # will fail. Raises Value error
matrix3 = EvenMatrix (3, 7)
matrix2.setValue(0, 0, -3)
matrix2.setValue(0, 1, 3) # cell at row 0, column 1 changed to value 3 
matrix2.setValue(0, 2, 1)
matrix2.setValue(1, 0, -2)
matrix2.setValue(1, 1, -3)
matrix2.setValue(1, 2, 1)
matrix2.setValue(2, 0, 0.1)
matrix2.setValue(2, 1, -2)
matrix2.setValue(2, 2, 1)
matrixResult = Multiplication().operate(matrix2, matrix3)
print(matrix1)
print(matrix2)
print(matrix3)
print(matrixResult)
```

## For Developer
### How to Push to Upload to PyPi

```shell script
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ <packagename>

# command to upload to the pypi repository
twine upload dist/*
pip install <packagename>
```