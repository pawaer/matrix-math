from matrixmath.Matrix import Matrix
from matrixmath.EvenMatrix import EvenMatrix
from matrixmath.Multiplication import Multiplication
import pytest

# Remark: This repositiory is just for testing python packages skills. In production we would use e.g. numpy
TOLERANCE = 1e-9  # tolerance results from float multiplication without numpy.


def test_scalar1_Matrix():
    """
    Testing scalar multiplication with float and Matrix. All values of matrix equal except one specialValue to provide
    some heterogeneity
        - Dimension of result shall be same
        - resulting matrix get multiplied with scalar value
    """

    defaultValue = 1.1  # default cell value
    specialValue = 3.3  # special cell value
    specialCell = [12, 13]  # special cell

    scalar = 0.7  # scalar factor
    matrix1 = Matrix(44, 45, defaultValue)

    matrix1.setValue(specialCell[0], specialCell[1], specialValue)
    # TODO {Low} research for alternatives for Multiplication-Constructor. maybe sth like a static class?
    result = Multiplication().operate(scalar, matrix1)

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert isCorrect(result.data[row][col], scalar * specialValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))
            else:
                assert isCorrect(result.data[row][col], scalar * defaultValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))


def test_scalar1_EvenMatrix():
    """
    Testing scalar multiplication with float and EvenMatrix. All values of matrix equal except one specialValue to
    provide some heterogeneity
        - Dimension of result shall be same
        - resulting matrix get multiplied with scalar value
    """

    defaultValue = 1.1  # default cell value
    specialValue = 3.3  # special cell value
    specialCell = [12, 13]  # special cell

    scalar = 0.7  # scalar factor
    matrix1 = EvenMatrix(44, defaultValue)

    matrix1.setValue(specialCell[0], specialCell[1], specialValue)
    result = Multiplication().operate(scalar, matrix1)

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert isCorrect(result.data[row][col], scalar * specialValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))
            else:
                assert isCorrect(result.data[row][col], scalar * defaultValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))


def test_scalar2_Matrix():
    """
    Testing scalar multiplication with integer and Matrix. All values of matrix equal except one specialValue to provide
    some heterogeneity
        - Dimension of result shall be same
        - resulting matrix get multiplied with scalar value
    """

    defaultValue = 7  # default cell value
    specialValue = 10  # special cell value
    specialCell = [2, 3]  # special cell

    scalar = 3  # scalar factor
    matrix1 = Matrix(4, 45, defaultValue)

    matrix1.setValue(specialCell[0], specialCell[1], specialValue)
    result = Multiplication().operate(scalar, matrix1)

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert isCorrect(result.data[row][col], scalar * specialValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))
            else:
                assert isCorrect(result.data[row][col], scalar * defaultValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))


def test_scalar2_EvenMatrix():
    """
    Testing scalar multiplication with integer and EvenMatrix. All values of matrix equal except one specialValue to
    provide some heterogeneity
        - Dimension of result shall be same
        - resulting matrix get multiplied with scalar value
    """

    defaultValue = 7  # default cell value
    specialValue = 10  # special cell value
    specialCell = [2, 3]  # special cell

    scalar = 3  # scalar factor
    matrix1 = EvenMatrix(4, defaultValue)

    matrix1.setValue(specialCell[0], specialCell[1], specialValue)
    result = Multiplication().operate(scalar, matrix1)

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert isCorrect(result.data[row][col], scalar * specialValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))
            else:
                assert isCorrect(result.data[row][col], scalar * defaultValue, TOLERANCE), (
                    "row {0} column {1}".format(row, col))


def test_scalar3():
    """
    Testing scalar multiplication with multiple scalar factors
        - Dimension of result shall be same
        - resulting matrix get multiplied with scalar value
    """

    defaultValue = 7  # default cell value
    specialValue = 10  # special cell value
    specialCell = [2, 3]  # special cell

    scalar1 = 3  # scalar factor1
    scalar2 = 3.2  # scalar factor2
    matrix1 = EvenMatrix(4, defaultValue)

    matrix1.setValue(specialCell[0], specialCell[1], specialValue)
    result = Multiplication().operate(scalar2, Multiplication().operate(scalar1, matrix1))

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert isCorrect(result.data[row][col], scalar1 * scalar2 * specialValue, TOLERANCE), (
                    "row {0} column {1}")
            else:
                assert isCorrect(result.data[row][col], scalar1 * scalar2 * defaultValue, TOLERANCE), (
                    "row {0} column {1}")


def test_general1_Matrix():
    """
    Testing scalar multiplication with scalar factor as second argument and Matrix
        - Scalar factor is allowed only for the first argument yet
        => Shall raise ValueError
    """
    matrix1 = Matrix(4, 8)

    with pytest.raises(ValueError):
        Multiplication().operate(matrix1, 2)


def test_general1_EvenMatrix():
    """
    Testing scalar multiplication with scalar factor as second argument and EvenMatrix
        - Scalar factor is allowed only for the first argument yet
        => Shall raise ValueError
    """
    matrix1 = EvenMatrix(4)

    with pytest.raises(ValueError):
        Multiplication().operate(matrix1, 2)


def test_matrix1_Matrix():
    """
    Testing Matrix with Matrix multiplication.
        - Dimension of two matrixes don't fit
        => Shall raise ValueError
    """
    matrix1 = Matrix(5, 8)
    matrix2 = Matrix(7, 5, -11)

    with pytest.raises(ValueError):
        Multiplication().operate(matrix1, matrix2)


def test_matrix1_EvenMatrix():
    """
    Testing EvenMatrix with EvenMatrix multiplication.
        - Dimension of two matrixes don't fit
        => Shall raise ValueError
    """
    matrix1 = EvenMatrix(4)
    matrix2 = EvenMatrix(5)

    with pytest.raises(ValueError):
        Multiplication().operate(matrix1, matrix2)


def test_matrix2_Matrix():
    """
    Testing Matrix with Matrix multiplication.
        - Dimension of resulting matrix shall fit
        - Resulting object shall be of class Matrix but not of EvenMatrix
        => Shall raise ValueError
    """
    matrix1 = Matrix(3, 2)
    matrix2 = Matrix(2, 4, -11)
    expectedResult = Matrix(3, 4)

    #  matrix 1: [3  2]     matrix 2: [1 3 5 7]     expectedResult: [5 9  19 25]
    #            [5  4]  *            [1 0 2 2]  =                  [9 15 33 43]
    #            [5  1]                                             [6 15 27 37]

    # matrix1 initialization
    matrix1.setValue(0, 0, 3)
    matrix1.setValue(0, 1, 2)
    matrix1.setValue(1, 0, 5)
    matrix1.setValue(1, 1, 4)
    matrix1.setValue(2, 0, 5)
    matrix1.setValue(2, 1, 1)

    # matrix2 initialization
    matrix2.setValue(0, 0, 1)
    matrix2.setValue(0, 1, 3)
    matrix2.setValue(0, 2, 5)
    matrix2.setValue(0, 3, 7)
    matrix2.setValue(1, 0, 1)
    matrix2.setValue(1, 1, 0)
    matrix2.setValue(1, 2, 2)
    matrix2.setValue(1, 3, 2)

    # expectedResult initialization
    expectedResult.setValue(0, 0, 5.0)
    expectedResult.setValue(0, 1, 9.0)
    expectedResult.setValue(0, 2, 19.0)
    expectedResult.setValue(0, 3, 25.0)
    expectedResult.setValue(1, 0, 9.0)
    expectedResult.setValue(1, 1, 15.0)
    expectedResult.setValue(1, 2, 33.0)
    expectedResult.setValue(1, 3, 43.0)
    expectedResult.setValue(2, 0, 6.0)
    expectedResult.setValue(2, 1, 15.0)
    expectedResult.setValue(2, 2, 27.0)
    expectedResult.setValue(2, 3, 37.0)

    result = Multiplication().operate(matrix1, matrix2)

    assert (result.getDimension() == [3, 4])
    assert (isinstance(result, Matrix)), "Shall be Matrix"
    assert (not isinstance(result, EvenMatrix)), "Shall not be EvenMatrix"
    assert (result.isEqualTo(expectedResult))


def test_matrix2_EvenMatrix():
    """
    Testing EvenMatrix with EvenMatrix multiplication.
        - Dimension of two matrixes don't fit
        => Shall raise ValueError
    """
    matrix1 = EvenMatrix(3)
    matrix2 = EvenMatrix(3, -254)
    expectedResult = EvenMatrix(3)

    #  matrix 1: [3  2   3]     matrix 2: [ 1  3  5]     expectedResult: [-1 0  31]
    #            [5  4  -1]  *            [ 1  0  2]  =                  [11 18 29]
    #            [5  1   5]               [-2 -3  4]                     [-4 0  47]
    # matrix1 initialization
    matrix1.setValue(0, 0, 3)
    matrix1.setValue(0, 1, 2)
    matrix1.setValue(0, 2, 3)
    matrix1.setValue(1, 0, 5)
    matrix1.setValue(1, 1, 4)
    matrix1.setValue(1, 2, -1)
    matrix1.setValue(2, 0, 5)
    matrix1.setValue(2, 1, 1)
    matrix1.setValue(2, 2, 5)

    # matrix2 initialization
    matrix2.setValue(0, 0, 1)
    matrix2.setValue(0, 1, 3)
    matrix2.setValue(0, 2, 5)
    matrix2.setValue(1, 0, 1)
    matrix2.setValue(1, 1, 0)
    matrix2.setValue(1, 2, 2)
    matrix2.setValue(2, 0, -2)
    matrix2.setValue(2, 1, -3)
    matrix2.setValue(2, 2, 4)

    # expectedResult initialization
    expectedResult.setValue(0, 0, -1)
    expectedResult.setValue(0, 1, 0)
    expectedResult.setValue(0, 2, 31)
    expectedResult.setValue(1, 0, 11)
    expectedResult.setValue(1, 1, 18)
    expectedResult.setValue(1, 2, 29)
    expectedResult.setValue(2, 0, -4)
    expectedResult.setValue(2, 1, 0)
    expectedResult.setValue(2, 2, 47)

    result = Multiplication().operate(matrix1, matrix2)

    assert (result.getDimension() == [3, 3])
    assert (isinstance(result, Matrix)), "Shall be Matrix (parent)"
    assert (isinstance(result, EvenMatrix)), "Shall be EvenMatrix"
    assert (result.isEqualTo(expectedResult))


def isCorrect(measured, expected, tolerance):
    '''
    deviation unavoidable with float values
    :param measured:
    :param expected:
    :param tolerance:
    :return: True (in tolerance) or False (otherside of tolerance)
    '''
    return abs(measured - expected) < tolerance
