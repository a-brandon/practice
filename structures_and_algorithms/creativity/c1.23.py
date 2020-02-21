"""C-1.23

Give an example of a Python code fragment that attempts to write
an element to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception tha results, and print
the following message: "Don't try buffer overflow attacks in Python!"""""

try:
    a_list = [1, 2, 3]
    a_list[4] = 6
except IndexError:
    print("Don't try buffer overflow attacks in Python!")
