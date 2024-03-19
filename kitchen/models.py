from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant_kitchen import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cooks"
        verbose_name_plural = "cooks"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cooks"
    )

    def __str__(self):
        return f"Name: {self.name}. Price: {self.price}."
