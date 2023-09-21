import unittest



def divide_numbers(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError(f"Division by Zero is not allowed. ")
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError(f"Invalid input. Please enter integers. ")
        result = num1 / num2
        return result



    except ValueError as a:
        return str(a)
    except ZeroDivisionError as b:
        return str(b)
    except Exception as e:
        return "An error occurred."

# num1 = int(input("Enter the first integer number "))
# num2 = int(input("Enter the second integer number "))
#
# result_num = divide_numbers(num1, num2)
# print(result_num)



class TestDivideNumbers(unittest.TestCase):

    def test_valid_division(self):
        """
        Test that the function correctly divides two integers.
        """
        self.assertEqual(divide_numbers(4, 2), 2.0)

    def test_divide_by_zero(self):
        """
        Test that division by zero raises a ZeroDivisionError.
        """
        self.assertEqual(divide_numbers(4, 0), "Division by zero is not allowed.")

    def test_invalid_input1(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers(4.5, 2), "Invalid input. Please enter integers.")

    def test_invalid_input2(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers("4", 2), "Invalid input. Please enter integers.")

    def test_invalid_input3(self):
        """
        Test that non-integer input raises a ValueError.
        """
        self.assertEqual(divide_numbers(4, "2"), "Invalid input. Please enter integers.")

if __name__ == "__main__":
    unittest.main()


