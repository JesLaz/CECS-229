class Matrix:

    def __init__():  # FIXME: Replace with your code
        pass

    def __add__(self, other):
        pass  # FIXME: REPLACE WITH IMPLEMENTATION

    def __sub__(self, other):
        pass  # FIXME: REPLACE WITH IMPLEMENTATION

    def __mul__(self, other):
        if type(other) == float:
            print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  # REPLACE
        elif type(other) == Matrix:
            print("FIXME: Insert implementation of MATRIX-MATRIX multiplication")  # REPLACE
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  # REPLACE
        else:
            print("ERROR: Unsupported Type.")
        return

    def __rmul__(self, other):
        if type(other) == float:
            print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  # REPLACE
        else:
            print("ERROR: Unsupported Type.")
        return

    def __str__(self):
        """prints the column """

