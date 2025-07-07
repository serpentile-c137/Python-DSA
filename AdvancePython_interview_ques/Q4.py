# Explain args and kwargs


def func(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ",kwargs)

func(1, 2, 3, a=4, b=5)

# Allows flexible input to functions.
# args:  (1, 2, 3)
# kwargs:  {'a': 4, 'b': 5}