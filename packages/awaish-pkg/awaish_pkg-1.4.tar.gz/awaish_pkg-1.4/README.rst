Project title
=============

`awaish_pkg` is a Python package that contains a collection of utility functions and a stack data structure. It is designed to assist with various operations, including mathematical calculations, sorting algorithms, and text processing.

Features
--------

1. **Utility Functions:**

   - List manipulation (sum of digits, separating positive and negative numbers, etc.)
   - Fibonacci series generator
   - Prime number checker
   - Number patterns (palindrome pyramid)
   - Sorting algorithms

2. **Stack Data Structure:**

   - Implement stack operations: push, pop, peek, check if empty/full, and display.

Installation
------------

To install the package, simply run:

.. code-block:: sh

   pip install awaish_pkg

Documentation
-------------

For detailed documentation, see:
`GitHub <https://github.com/abuawaish/awaish_pkg>`__

Author
------

Created by:
`abuawaish7 <https://www.github.com/abuawaish>`__

Badges
------

.. image:: https://badge.fury.io/py/awaish_pkg.svg
   :target: https://pypi.org/project/awaish_pkg/

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT

Usage
-----

To use the package in your Python script:

.. code-block:: python

   from awaish_pkg import Stack, UtilityFunctions

   # Example usage of stack
   stack = Stack()
   stack.run_stack()

   # Example usage of utility functions
   UtilityFunctions.add_list_index_element()
