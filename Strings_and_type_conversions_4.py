# You know about ascii values right
# WE can get them in python by using ordinal number function

string = 'A'

print(ord(string))

a = 'h'

print(ord(a))


""" NOW THERE ARE INDEXING IN PYTHON """
""" +ve indexing == start from 0 to infinity"""
""" -ve indexing == start from -1 to -infinity"""

b = 'TIGGLY'

# positive indexing
print(b[0])
print(b[1])
print(b[2])


# negative indexing
print(b[-1])
print(b[-2])


# We can also write it like this
print(b[4],b[-6])



"""WE CAN ALSO DO STRING SLICING"""

c = 'NOOBS'
print(c[0:3:1])       # SYNTAX --> variable_name[start:end:interval]
print(c[0:5:2])
print(c[::2])   # Here python assummes some default values like start and end point of the string
print(c[-1:-5:-1])   # We can also do it negative



"""    *****************  TYPE CONVERSION   ********************    """


#You can convert a value from one type to another using these built-in functions:
# int , float, str, bool

a = '67'
print(type(a))
a = int(a)
print(type(a))  

""""
COMMON ERROR 
b = '67.69'
This wont be converted into a int but will convert into float"""


b = '67.69'
print(type(b))
print(float(b))  # Here we forced b to become float for only a moment
print(type(b))


# NOW BOOL FUNCTION IS KINDA INTERESTINNG
# ONLY 7 VALUES HOLD FALSE OTHER ALL HOLDS TRUE
# FALSE, 0, 0.0, "", [], {}, ()

# YOU CAN ALSO ICROSS CHECK IF YOU WANT TO
