from matrixmath.Matrix import Matrix


def test_init1():
    matrix = Matrix(14, 4, 3)
    assert (matrix.getValue(9, 3) == 3)


def test_init2():
    matrix = Matrix(4, 13)
    assert (matrix.getValue(3, 12) == 0)


def test_changeValue1():
    matrix = Matrix(40, 40, 0)
    matrix.setValue(10, 10, 100)
    assert (matrix.getValue(10, 10) == 100)
    matrix.setValue(39, 39, -10)
    assert (matrix.getValue(39, 39) == -10)
