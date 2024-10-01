from lib.report_length import *

def test_report_length_for_howdy():
    result = report_length("Howdoo")
    assert result == "This string was 6 characters long."
