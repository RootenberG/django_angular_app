from django.db import models


class BalanceSheet(models.Model):
    name = models.CharField(max_length=30)
    year_2019 = models.CharField(max_length=30)
    year_2018 = models.CharField(max_length=30)
    year_2017 = models.CharField(max_length=30)
    year_2016 = models.CharField(max_length=30)

