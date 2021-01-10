from matrixmath.Matrix import Matrix
from matrixmath.EvenMatrix import EvenMatrix
from matrixmath.Multiplication import Multiplication


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
    result = Multiplication().operate(scalar, matrix1)

    assert result.getDimension() == matrix1.getDimension(), (
        "resultDimension {0} unequal matrix1Dimension {1}".format(result.getDimension(), matrix1.getDimension()))

    for row in range(result.rowCount):
        for col in range(result.columnCount):
            if row == specialCell[0] and col == specialCell[1]:
                assert result.data[row][col] == scalar * specialValue, (" 1row {0} column {1}".format(row, col))
            else:
                assert result.data[row][col] == scalar * defaultValue, ("row {0} column {1}".format(row, col))


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
                assert result.data[row][col] == scalar * specialValue, (" 1row {0} column {1}".format(row, col))
            else:
                assert result.data[row][col] == scalar * defaultValue, ("row {0} column {1}".format(row, col))


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
                assert result.data[row][col] == scalar * specialValue, ("row {0} column {1}".format(row, col))
            else:
                assert result.data[row][col] == scalar * defaultValue, ("row {0} column {1}".format(row, col))


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
                assert result.data[row][col] == scalar * specialValue, ("row {0} column {1}".format(row, col))
            else:
                assert result.data[row][col] == scalar * defaultValue, ("row {0} column {1}".format(row, col))
