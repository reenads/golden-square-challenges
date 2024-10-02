from lib.string_builder import *

#returns an empty string

def test_returns_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

#returns a string with words added

def test_string_with_words_added():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.output() == "Hello"

#returns a string with multiple words
def test_string_multiple_words():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add("Mum")
    assert string_builder.output() == "HelloMum"

#check the length of the built up string

def test_multiply_strings_length_of_built_up_String():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add("Mum")
    assert string_builder.size() == 8