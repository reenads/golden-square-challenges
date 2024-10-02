from lib.high_value import *

#does the function correctly identify the higher number
def test_if_first_number_is_higher():
    highvalue = HighValue(8,4)
    actual = highvalue.get_highest()
    expected  = "First value is higher"
    assert actual == expected

def test_is_second_number_is_higher():
    highvalue = HighValue(4,8)
    actual = highvalue.get_highest()
    expected  = "Second value is higher"
    assert actual == expected

def test_if_numbers_are_equal():
    highvalue = HighValue(4,4)
    actual = highvalue.get_highest()
    expected  = "Values are equal"
    assert actual == expected

#does the add function increase the higher number
# def test_does_the_number_increase():
#     highvalue = HighValue(8,4)
#     highvalue.get_highest = 8
#     actual =  highvalue.add(5, highvalue.get_highest)
#     expected = 13
#     assert actual == expected
# highvalue.add(5, highvalue.get_highest)

def test_does_the_add_function_increase_the_first_val():
    highvalue = HighValue(8,4)
    highvalue.add(5, "first")
    assert highvalue.value_first == 13

def test_does_the_add_function_increase_the_second_val():
    highvalue = HighValue(3,10)
    highvalue.add(5, "second")
    assert highvalue.value_second == 15

def test_does_the_add_function_increase_if_val_is_0():
    highvalue = HighValue(10,3)
    highvalue.add(0, "first")
    assert highvalue.value_first == 10

def test_does_the_add_function_increase_if_val_is_0_second():
    highvalue = HighValue(3,10)
    highvalue.add(0, "second")
    assert highvalue.value_second == 10

def test_does_the_add_function_increase_if_val_is_neg_num():
    highvalue = HighValue(-3,-5)
    highvalue.add(5, "first")
    assert highvalue.value_first == 2