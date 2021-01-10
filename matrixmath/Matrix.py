class Matrix:

    def __init__(self, rowCount, columnCount, initialValue=0):
        """ Creating Matrix with of certain size with predefined initializer value

        Attributes:
            rowCount (int) representing the number of rows
            columnCount (int) representing the number of rows
            initialValue (float) the initial value. If not set it is 0
        """

        self.rowCount = rowCount
        self.columnCount = columnCount
        self.data = [[initialValue for col in range(columnCount)] for row in range(rowCount)]

        print("Created matrix: %drows x %dcolumns with preinitialized value '%.2f'" % (
            rowCount, columnCount, initialValue))

    def __repr__(self):

        """Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """


        for i in range(self.rowCount):
            for j in range(self.columnCount):
                print(self.data[i][j], end="\t")  # tab between each row

            print('')  # new line
        return "rowSize {}, columnSize {}".format(self.rowCount, self.columnCount)
    def getValue(self, row, column):
        """ Function returns a value of a certain row column pair
        Args:
            row (int) repesenting the row
            column (int) repesenting the column
            value (float) repesenting the value
        Returns:
            None
        """
        value = self.data[row][column]

        print("Value of %d x %d: %.2f" % (row, column, value))
        return value

    def setValue(self, row, column, value):
        """ Function set a certain value of a row column pair
        Args:
            row (int) repesenting the row
            column (int) repesenting the column
            value (float) repesenting the value
        Returns:
            None
        """
        self.data[row][column] = value

    def getDimension(self):
        """ Function returns dimension of Matrix
        Args:
        Returns:
            Tuple(row, column)
        """
        return [self.rowCount, self.columnCount]

    def isEqualTo(self, otherMatrix):
        """ Function checks equality to other matrix
        Args: otherMatrix (Matrix) representing other matrix to compare
        Returns:
            True (Equality) or False (Inequality)
        """
        if self.getDimension() != otherMatrix.getDimension():
            return False

        for row in range(self.rowCount):
            for col in range(self.columnCount):
                selfValue = self.getValue(row, col)
                otherMatrixValue = otherMatrix.getValue(row, col)
                if selfValue != otherMatrixValue:
                    print("in row {0} column {1} selfValue {2} otherMatrixValue {3}".format(row, col, selfValue,
                                                                                            otherMatrixValue))
                    return False

        return True
