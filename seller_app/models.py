from django.db import models

# Create your models here.
# admin_app/models.py
from django.db import models

class Plants(models.Model):
    Name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
