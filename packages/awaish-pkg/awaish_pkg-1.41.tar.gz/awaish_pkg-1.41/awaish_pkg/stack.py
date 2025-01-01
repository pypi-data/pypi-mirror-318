class Stack:
    def __initialize(self):
        self.__stack = []
        self.__limit = int(input("Enter the limit of the stack : "))
        """
        Initializes the stack with a fixed size limit.

        Args:
            limit (int): The maximum number of elements the stack can hold.
        """

    def __push(self, element: int) -> None:
        """
        Pushes an element onto the stack if it's not full.

        Args:
            element (int): The element to be pushed onto the stack.
        """
        if self.__is_full():
            print("\nStack is full. Unable to push the element.")
        else:
            self.__stack.append(element)
            print(f"\n{element} has been pushed onto the stack.")
            print("Current stack:", self.__stack)

    def __pop(self) -> int | None:
        """
        Removes and returns the top element of the stack if it's not empty.

        Returns:
            int: The top element of the stack.
        """
        if self.__is_empty():
            print("\nStack is empty. Nothing to pop.")
            return None
        else:
            element = self.__stack.pop()
            print(f"\n{element} has been popped from the stack.")
            print("Current stack:", self.__stack)
            return element

    def __peek(self) -> int | None:
        """
        Returns the top element of the stack without removing it.

        Returns:
            int: The top element of the stack.
        """
        if self.__is_empty():
            print("\nStack is empty. No top element.")
            return None
        else:
            return self.__stack[-1]

    def __is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.__stack) == 0

    def __is_full(self) -> bool:
        """
        Checks whether the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return len(self.__stack) == self.__limit

    def __size(self) -> int:
        """
        Returns the current size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.__stack)

    def __display(self) -> None:
        """
        Displays all elements in the stack.
        """
        if self.__is_empty():
            print("\nThe stack is empty.")
        else:
            print("\nCurrent stack (top to bottom):")
            for element in reversed(self.__stack):
                print(element)

    def run_stack(self) -> None:
        """
        Provides an interactive interface for performing stack operations.
        """
        self.__initialize()
        while True:
            print("\nChoose an operation:")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Check if Empty")
            print("5. Check if Full")
            print("6. Display Stack")
            print("7. Get Size")
            print("8. Exit")

            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                element = int(input("\nEnter the element to push: "))
                self.__push(element)
            elif choice == 2:
                self.__pop()
            elif choice == 3:
                top_element = self.__peek()
                if top_element is not None:
                    print(f"\nThe top element is: {top_element}")
            elif choice == 4:
                print("\nIs the stack empty?", self.__is_empty())
            elif choice == 5:
                print("\nIs the stack full?", self.__is_full())
            elif choice == 6:
                self.__display()
            elif choice == 7:
                print(f"\nThe size of the stack is: {self.__size()}")
            elif choice == 8:
                print("\nExiting the stack program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid operation.")

s: Stack = Stack()
s.run_stack()