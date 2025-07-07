# What’s the Difference Between deep copy and shallow copy?


import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)       # Shallow
c = copy.deepcopy(a)   # Deep

# Shallow → new outer list but inner lists same
# Deep → completely new
