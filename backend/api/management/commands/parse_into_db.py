import requests as req
from bs4 import BeautifulSoup
import time

from django.core.management.base import BaseCommand

from ...models import BalanceSheet


class Command(BaseCommand):
    help = "This command parse and store data from https://finance.yahoo.com/quote/GOOG/balance-sheet into db"

    def handle(self, *args, **options):
        resp = req.get("https://finance.yahoo.com/quote/GOOG/balance-sheet?p=GOOG")
        soup = BeautifulSoup(resp.text, "lxml")

        mydivs = soup.find(
            "div", {"class": "W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)"}
        )
        spans = mydivs.findAll("span")[5:]  # skips column's names
        spans = [i.encode_contents().decode("utf-8") for i in spans]

        for i in range(0, len(spans) - 1, 5):
            name, year_2019, year_2018, year_2017, year_2016 = spans[i : i + 5]
            new_record = BalanceSheet(
                name=name,
                year_2019=year_2019,
                year_2018=year_2018,
                year_2017=year_2017,
                year_2016=year_2016,
            )
            new_record.save()
