from matrixmath.EvenMatrix import EvenMatrix


def test_init1():
    evMatrix = EvenMatrix(14, 3)
    assert (evMatrix.getValue(13, 13) == 3)


def test_init2():
    evMatrix = EvenMatrix(4, 13)
    assert (evMatrix.getValue(3, 2) == 13)


def test_changeValue1():
    evMatrix = EvenMatrix(40, 0)
    evMatrix.setValue(10, 10, 100)
    assert (evMatrix.getValue(10, 10) == 100)
    evMatrix.setValue(39, 39, -10)
    assert (evMatrix.getValue(39, 39) == -10)
