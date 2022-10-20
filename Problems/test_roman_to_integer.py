from roman_to_integer import *
#above: import everything from file
#namespacing: what do you have access to and how do you have to call it?

def test_single_numeral():
    assert romanToInt("I") == 1

def test_double_numeral():
    assert romanToInt("II") == 2

def test_triple_numeral():
    assert romanToInt("III") == 3
