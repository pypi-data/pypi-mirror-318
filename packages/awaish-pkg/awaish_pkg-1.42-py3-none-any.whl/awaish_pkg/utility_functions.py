class UtilityFunctions:
    """
    A collection of utility functions grouped into a single class for better organization.
    Includes implementations for stack operations, list processing, number patterns, and more.
    """

    @staticmethod
    def add_list_index_element():
        """
        Sums the digits of each integer in a user-provided list and creates a new list with the results.
        """
        ls = []
        sum_of_index_element = []
        size = int(input("Enter the limit of the list: "))
        for i in range(size):
            ls.append(int(input(f"Enter the element at {i} index: ")))

        print("\nThe original list is:", ls)

        for num in ls:
            digit_sum = sum(int(digit) for digit in str(abs(num)))
            sum_of_index_element.append(digit_sum)

        print("\nAfter summing the digits of each element, the list is:", sum_of_index_element)

    @staticmethod
    def find_positive_and_negative():
        """
        Separates positive and negative numbers in a user-provided list and calculates their sums.
        """
        lim = int(input("Enter the limit of the list: "))
        ls = [int(input(f"Enter the element at {i} index: ")) for i in range(lim)]
        positive = [num for num in ls if num > 0]
        negative = [num for num in ls if num < 0]

        print("\nThe original list is:", ls)
        if positive:
            print("\nPositive numbers:", positive)
            print("Sum of positive numbers:", sum(positive))
        else:
            print("\nNo positive numbers were provided.")

        if negative:
            print("\nNegative numbers:", negative)
            print("Sum of negative numbers:", sum(negative))
        else:
            print("\nNo negative numbers were provided.")

    @staticmethod
    def factor_finder():
        """
        Finds and prints the factors of a user-provided number, along with their sum.
        """
        number = int(input("Enter any number: "))
        factors = [i for i in range(1, number + 1) if number % i == 0]

        print(f"\nThe factors of {number} are:", factors)
        print(f"The sum of the factors is: {sum(factors)}")

    @staticmethod
    def count_vowel_and_spaces():
        """
        Counts vowels and spaces in a user-provided text input.
        """
        text = input("Enter some text: ")
        vowels = 'aeiouAEIOU'
        vowel_list = [char for char in text if char in vowels]
        space_count = text.count(' ')

        print("\nThe original text is:", text)
        print(f"Total vowels: {len(vowel_list)} ({vowel_list})")
        print(f"Total spaces: {space_count}")

    @staticmethod
    def prime_finder():
        """
        Determines whether a user-provided number is prime.
        """
        num = int(input("Enter any number to check if it's prime: "))
        if num < 2:
            print(f"The number {num} is not a prime number.")
            return

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"The number {num} is not a prime number.")
                return
        print(f"The number {num} is a prime number.")

    @staticmethod
    def even_and_odd():
        """
        Separates a user-provided list of numbers into even and odd numbers and prints them.
        """
        lim = int(input("Enter the limit of the list: "))
        lst = [int(input(f"Enter the element at {i} index: ")) for i in range(lim)]
        even = [num for num in lst if num % 2 == 0]
        odd = [num for num in lst if num % 2 != 0]

        if even:
            print("List of even numbers:", even)
        else:
            print("No even numbers were provided.")

        if odd:
            print("List of odd numbers:", odd)
        else:
            print("No odd numbers were provided.")

    @staticmethod
    def fibonacci_series():
        """
        Generates a Fibonacci series based on user input.
        """
        n = int(input("Enter how many terms you want in the series: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    @staticmethod
    def selection_sort(arr):
        """
        Sorts a list of integers in ascending order using the selection sort algorithm.

        Args:
            arr (list): A list of integers to sort.

        Returns:
            list: The sorted list.
        """
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def palindrome_number_pattern(n):
        """
        Prints a number pyramid pattern resembling a palindrome structure.
        """
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            print(" ".join(map(str, range(i, 0, -1))), end=" ")
            print(" ".join(map(str, range(2, i + 1))))

