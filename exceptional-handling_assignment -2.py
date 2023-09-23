#!/usr/bin/env python
# coding: utf-8

# Ans 1: When creating a custom exception in Python, we use the Exception class as a base class for several reasons:
# 
# The Exception class provides the base functionality needed to handle exceptions. This includes methods for getting a string representation of the exception and for accessing the traceback.
# By inheriting from the Exception class, we ensure that our custom exception is treated like other exceptions in Python. This means it can be caught using an except block and it will be handled correctly by debugging and logging tools.
# Inheriting from the Exception class also allows us to add custom behavior or data to our exceptions. For example, we can override the constructor to accept additional arguments, or add new methods that provide more information about the error.
# Here’s an example of a custom exception that inherits from the Exception class:

# In[1]:


class CustomError(Exception):
    """A user-defined error which inherits from the Exception class."""
    pass

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print(f"Caught an exception: {e}")


# In[2]:


#Ans 2 : 
import inspect
import pprint

def print_exception_hierarchy(hierarchy, current_class, indent=-2):
    if indent != -2:
        hierarchy.append('  ' * indent + current_class.__name__)
    for subclass in current_class.__subclasses__():
        print_exception_hierarchy(hierarchy, subclass, indent + 2)

hierarchy = []
print_exception_hierarchy(hierarchy, BaseException)
pprint.pprint('\n'.join(hierarchy))


# Ans 3 : The ArithmeticError class in Python serves as the base class for those built-in exceptions that are raised due to various arithmetic errors. The following errors are defined in the ArithmeticError class:
# 
# ZeroDivisionError: This error is raised when the second argument of a division or modulo operation is zero. Here’s an example:

# In[3]:


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# In[4]:


import math
try:
    result = math.exp(1000)
except OverflowError:
    print("Error: The number is too large.")


# ANS 4: The LookupError class in Python serves as the base class for exceptions that are raised when a key or index used on a mapping or sequence is invalid. It is generally considered a base class from which other subclasses should inherit. The following errors are defined in the LookupError class:
# 
# 

# In[6]:


#KeyError: This error is raised when a dictionary key is not found. For example:

employees = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
try:
    print(employees['Michael'])
except KeyError:
    print("Error: Key not found.")


# In[7]:


# IndexError: This error is raised when a sequence subscript (index) is out of range. For example:
test_list = [1, 2, 3, 4]
try:
    print(test_list[4])
except IndexError:
    print("Error: Index out of range.")


# Ans 5 : The ImportError in Python is raised when an import statement fails to find the module definition or when a from ... import ... fails to find a name that is to be imported. This error generally occurs if there is an invalid declaration of import statement for module importing.
# 
# For example, if you try to import a module that does not exist or is not installed, Python will raise an ImportError. Here’s an example:

# In[9]:


try:
    import numpy as np
except ModuleNotFoundError:
    print("Error: The numpy module is not installed.")
    
    "As it did not gave error beacuse numpy is already imported"


# In[10]:


try:
    import non_existent_module
except ImportError:
    print("Error: The module does not exist.")


# Ans 6 : Here are some best practices for handling exceptions in Python:
# 
# Never use exceptions for flow-control: Exceptions exist for exceptional situations1. They are not part of normal execution. For example, the ‘find’ method on a string returns -1 if the pattern isn’t found, but indexing beyond the end of a string raises an exception1. Not finding the string is normal execution.
# 
# Handle exceptions at the level that knows how to handle them: The best place to handle an exception is that piece of code that can handle the exception. For some exceptions, like programming errors (e.g. IndexError, TypeError, NameError etc.) exceptions are best left to the programmer/user, because “handling” them will just hide real bugs1.
# 
# Design for failure: Plan ahead by considering possible failures and designing your program to handle them gracefully. This means anticipating edge cases and implementing appropriate error handlers.
# 
# Use descriptive error messages: Provide detailed error messages or logs that help users understand what went wrong and why.
# 
# Raise and catch exceptions properly: Use try, except, and finally blocks effectively3. Catch specific exceptions instead of using a generic except block.
# 
# Create custom exceptions for your specific use case: If the built-in exceptions do not meet your needs, you can create your own exceptions by subclassing the Exception class or one of its subclasses.

# In[ ]:




