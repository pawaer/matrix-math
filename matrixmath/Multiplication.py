from matrixmath.Matrix import Matrix
from matrixmath.EvenMatrix import EvenMatrix


class Multiplication:

    def scalarMultiplication(self, scalarFactor, second, debugTrace):
        """
        Perform a scalar multication with a factor
        :param scalarFactor: float or int
        :param second: matrix or Even Matrix
        :param debugTrace: display traces
        :return:
        """
        dimension = second.getDimension()
        result = Matrix(dimension[0], dimension[1])
        for row in range(dimension[0]):
            for column in range(dimension[1]):
                result.setValue(row, column, (scalarFactor * second.getValue(row, column)))

        if (debugTrace):
            print(result)

        return result

    def matrixMultiplication(self, first, second, debugTrace):
        dimFirst = first.getDimension()
        dimSecond = second.getDimension()

        # check if multiplication is possible
        if dimFirst[1] != dimSecond[0]:
            raise ValueError("first.column {0} shall be second.row {1}".format(dimFirst[0], dimSecond[1]))

        self.data = [[0 for col in range(dimSecond[1])] for row in range(dimFirst[0])]

        resultColumnCount = dimFirst[0]
        resultRowCount = dimSecond[1]

        result = [[0 for col in range(resultColumnCount)] for row in range(resultRowCount)]

        return result

    def operate(self, first, second, debugTrace=False):
        """
        Perform a multiplication of matrices
        :param first: first matrix
        :param second: second matrix
        :return: resulting matrix
        """

        print("%d %d" % (isinstance(first, Matrix), isinstance(second, Matrix)))

        # complex not handeled yet
        isFirstDigit = isinstance(first, (int, float))
        isFirstMatrix = isinstance(first, (Matrix, EvenMatrix))
        isSecondMatrix = isinstance(second, (Matrix, EvenMatrix))

        if (isFirstDigit and isSecondMatrix):
            result = self.scalarMultiplication(first, second, debugTrace)
        elif (isFirstMatrix and isSecondMatrix):
            result = self.matrixMultiplication(first, second, debugTrace)
        else:
            raise ValueError(
                "isFirstDigit '%d' isFirstMatrix '%d' isSecondMatrix '%d' can't be processed as multiplication" % (
                    isFirstDigit, isFirstMatrix, isSecondMatrix))

        # traces
        if (debugTrace):
            print(first)
            print("_____________________________________")
            print(second)
            print("_____________________________________")

        return result
