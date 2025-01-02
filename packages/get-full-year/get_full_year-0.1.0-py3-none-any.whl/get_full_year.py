from datetime import datetime

import requests

API_URL = "https://getfullyear.com/api"


class Year(int):
    def __init__(self, year: int):
        super().__init__()
        self.datetime = datetime(year, 1, 1)

    def is_leap(self) -> bool:
        # return self.value % 4 == 0 and (self.value % 100 != 0 or self.value % 400 == 0)
        return self % 4 == 0 and (self % 100 != 0 or self % 400 == 0)


class FullYear:
    def __init__(self):
        self.year: Year = None
        self.sponsored_by: str = None
        self._get_data()

    def _get_data(self) -> Year:
        with requests.get(f"{API_URL}/year") as response:
            self.year = Year(response.json()["year"])
            self.sponsored_by = response.json()["sponsored_by"]

    def __repr__(self):
        return f"<FullYear(year={self.year}, sponsored_by='{self.sponsored_by}')>"

    def __str__(self):
        return f"Year: {self.year} - Sponsored By: {self.sponsored_by}"


class console:
    # getfullyear Terms of Service requires the user to `console.log` the sponsored_by attribute.
    # However, Python does not have a `console.log` function. We implement this function here.
    def log(s: str):
        print(s)
