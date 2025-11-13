# Import module
import basic_functions.math_functions

basic_functions.math_functions.add(2,3) # Output: 5

# Import and use alias
import basic_functions.math_functions as mf

mf.add(2,3)

# Import just the function
from basic_functions.math_functions import add

add(2,3)