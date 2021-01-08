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

    def printAllValues(self):
        """ Function to print all values of the matrix. Just for deeper debugging
        Args:
            None
        Returns:
            None
        """

        for i in range(self.rowCount):
            for j in range(self.columnCount):
                print(self.data[i][j], end="\t")  # tab between each row

            print('')  # new line

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
