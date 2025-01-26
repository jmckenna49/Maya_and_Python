class ArrayReverser:
    def __init__(self, array):
        self.array = array

    def reverse(self):
        left = 0
        right = len(self.array) - 1

        while left < right:
            # Swap elements
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1

    def get_array(self):
        return self.array


def PerformCalcs():
    # Input array
    input_array = [1, 2, 3, 4, 5]
    print("Original array:", input_array)

    # Create an instance of ArrayReverser
    reverser = ArrayReverser(input_array)

    # Reverse the array
    reverser.reverse()

    # Print the reversed array
    print("Reversed array:", reverser.get_array())


if __name__ == "__main__":
    PerformCalcs()
