from matrixmath.Matrix import Matrix


class EvenMatrix(Matrix):
    def __init__(self, sizeHeightWidth, initialValue=0):
        """ Creating Matrix with of certain size with predefined initializer value

        Attributes:
            sizeHeightWidth (int) representing the number of rows and columns
            initialValue (float) the initial value. If not set it is 0
        """
        Matrix.__init__(self, sizeHeightWidth, sizeHeightWidth, initialValue)
