from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=64)
    img_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    listing_id = models.IntegerField(primary_key=True)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    bid = models.FloatField()


class Watchlist(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    watchlist_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Watchlists(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    watchlist_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
