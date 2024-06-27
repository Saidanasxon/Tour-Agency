from django.db import models


class TravelCategory(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places = 2)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    stars = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places = 2)

    def __str__(self):
        return self.name

class Travel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(TravelCategory, on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title