from django.db import models
from django.db.models import F, OuterRef, Subquery

class Expenses(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cash = models.PositiveBigIntegerField(blank=True)
    digital = models.PositiveBigIntegerField(blank=True)
    credit = models.PositiveBigIntegerField(blank=True)
    description = models.TextField(255,blank=True)

class Investments(models.Model):
    CATEGORIES = [("stock","stock"),("VFF","VFF"),("VMEEF","VMEEF"),\
                ("DCDE","DCDE"),("VESAF","VESAF"),("VEOF","VEOF"),\
                ("ETH","ETH"),("BTC","BTC")]
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10,choices=CATEGORIES,blank=False)
    amount = models.PositiveBigIntegerField(blank=False)

class Investment_tracking(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    acbs = models.PositiveBigIntegerField(blank=False)
    mio = models.PositiveBigIntegerField(blank=False)
    ssi = models.PositiveBigIntegerField(blank=True)
    dragon = models.PositiveBigIntegerField(blank=False)
    cash = models.PositiveBigIntegerField(blank=False)
    total_investment = models.PositiveBigIntegerField(blank=False)
    
    def save(self, *args, **kwargs):
        self.total_investment = self.acbs + self.mio + self.ssi + self.dragon + self.cash
        super().save(*args, **kwargs)
