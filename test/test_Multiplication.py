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
        result = Multiplication().operate(matrix1, matrix2)


def isCorrect(measured, expected, tolerance):
    '''
    deviation unavoidable with float values
    :param measured:
    :param expected:
    :param tolerance:
    :return: True (in tolerance) or False (otherside of tolerance)
    '''
    return abs(measured - expected) < tolerance
