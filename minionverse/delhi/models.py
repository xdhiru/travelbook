from django.db import models

# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=50)
    screen = models.DecimalField(max_digits=5, decimal_places=2)
    projector = models.DecimalField(max_digits=5, decimal_places=2)
    audio = models.DecimalField(max_digits=5, decimal_places=2)
    seats = models.DecimalField(max_digits=5, decimal_places=2)
    surroundings = models.DecimalField(max_digits=5, decimal_places=2)
    travel = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    remarks = models.TextField()

    def __str__(self):
        return self.name