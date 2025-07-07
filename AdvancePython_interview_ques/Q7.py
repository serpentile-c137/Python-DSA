# How to Write Unit Tests (Pytest Example)


def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5

# Run with:
# bash

# pytest test_script.py

# Output:
# ============================= test session starts =============================
# platform darwin -- Python 3.13.2, pytest-8.4.1, pluggy-1.6.0
# rootdir: /Users/shardulgore/Documents/Python_DSA
# configfile: pyproject.toml
# collected 1 item                                                                                                                                                             

# Q7.py .                                                                                                                                                                [100%]

# ============================= 1 passed in 0.01s =============================