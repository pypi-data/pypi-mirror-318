from get_full_year import Year


def test_year():
    year_2020 = Year(2020)
    assert year_2020.is_leap()
    assert str(year_2020) == "2020"
    assert int(year_2020) == 2020
    assert year_2020.datetime.year == 2020
    assert year_2020 + 45 == Year(2065)

    year_2021 = Year(2021)
    assert not year_2021.is_leap()
    assert str(year_2021) == "2021"
    assert int(year_2021) == 2021
    assert year_2021.datetime.year == 2021
    assert year_2021 - 45 == Year(1976)
