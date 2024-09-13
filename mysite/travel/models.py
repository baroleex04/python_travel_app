from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_name = models.CharField(max_length=200)
    embedded_code = models.CharField(max_length=500)
    add_date = models.DateTimeField("date added")
    price = models.CharField(max_length=200)
    menu_link = models.CharField(max_length=200)
    vote_like = models.IntegerField(default=0)
    def __str__(self):
        return self.embedded_code
    
class Address(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    ward = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.street_name
    
    
    