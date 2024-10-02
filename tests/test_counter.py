from lib.counter import *

#the counter initially is set at zero, lets test that

def test_counter_is_at_zero():
    counter = Counter ()
    assert counter.report() == "Counted to 0 so far."


def test_are_you_adding():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."