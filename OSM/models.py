from django.db import models

# Create your models here.


class Burger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return self.name

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('R', 'Ready'),
        ('D', 'Delivered'),
    ]
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    burger = models.ForeignKey(Burger, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    def __str__(self):
        return self.name



