# import pytest
#
# def test_sum():
#     total = 3 + 4
#     assert total == 7
# print(test_sum)

###############################################################

import datetime

def get_age(yyyy:int, m:int, d:int) -> int:
    dob = datetime.date(yyyy, m, d)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age

###############################################################

from calculate_age import get_age
def test_get_age():
    yyyy, mm, dd = map(int, "1996/07/11".split(""))
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 26