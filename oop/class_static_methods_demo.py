# class_static_methods_demo.py

class Calculator:
    """
    Demonstrates the difference between static and class methods.
    
    Attributes:
        calculation_type (str): Describes the type of calculation.
    """

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Does not access class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        Prints the class attribute 'calculation_type' before computing.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
