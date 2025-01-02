from datetime import datetime

from get_full_year import FullYear


def test_full_year():
    current_year = datetime.now()
    full_year = FullYear()
    assert full_year.year == current_year.year
    assert full_year.sponsored_by
    assert full_year.year.datetime.year == current_year.year
