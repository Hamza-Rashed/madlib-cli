
from madlib_cli.madlib import read_template , parse , merge

"""
test read template : 
any thing in txt file => should display
"""
def test_read_template():
    actual = read_template("/home/hamza/Desktop/401/labs/lab3/madlib-cli/textFiles/test.txt")
    expected = "Hello Gys I'm {first name} {last name} => hamza rashed"
    assert actual == expected

"""
test parse : 
any thing in txt file => should display with hiddin the variable and display it in list
"""

def test_parse():
    actual = parse("Hello every one .. My name is {first name} {last name} and I'm {age} years old . I'm {Adjective} and {Adjective}.")
    expected = "Hello every one .. My name is {} {} and I'm {} years old . I'm {} and {}.", ["first name","last name","age","Adjective", "Adjective"]
    assert actual == expected

"""
test merge : 
any thing in txt file => should display with merge all values from list indide it places
"""

def test_merge():
    actual = merge("Hello every one .. My name is {} {} and I'm {} years old . I'm {} and {}.", ["f","f","f","f", "f"])
    expected = "Hello every one .. My name is f f and I'm f years old . I'm f and f."
    assert actual == expected 