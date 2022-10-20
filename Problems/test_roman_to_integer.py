from roman_to_integer import *
#above: import everything from file
#namespacing: what do you have access to and how do you have to call it?

def test_single_numeral():
    assert romanToInt("I") == 1

def test_double_numeral():
    assert romanToInt("II") == 2

def test_triple_numeral():
    assert romanToInt("III") == 3

# def test_four():
#     assert romanToInt("IV") == 4

def test_five():
    assert romanToInt("V") == 5

# def test_nine():
#     assert romanToInt("IX") == 9

def test_sixteen():
    assert romanToInt("XVI") == 16

def test_twenty():
    assert romanToInt("XX") == 20

def test_fifty_eight():
    assert romanToInt("LVIII") == 58

def test_one_thousand_six_hundred():
    assert romanToInt("MDC") == 1600
