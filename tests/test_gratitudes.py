from lib.gratitudes import *

#what are we grateful for at the moment?
def test_when_nothing_to_be_grateful_for():
    gratitudes = Gratitudes()
    assert gratitudes.format() ==  "Be grateful for: "


#what are we grateful for onces we've added a gratitude
def test_one_thing_to_be_grateful_for():
    gratitudes = Gratitudes()
    gratitudes.add("snacks")
    assert gratitudes.format() ==  "Be grateful for: snacks"

#multiple things we are gratefull for in a list
def test_multiple_things_to_be_grateful_for():
    gratitudes = Gratitudes()
    gratitudes.add("snacks")
    gratitudes.add("health")
    gratitudes.add("friends")
    assert gratitudes.format() ==  "Be grateful for: snacks, health, friends"
