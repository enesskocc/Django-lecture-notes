from tabnanny import verbose
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()


    def __str__(self):
        return f"{self.number} - {self.first_name} - {self.last_name}"

    class Meta:
        ordering = ["number"] ## siralamayi numaralara göre yapacak. Default olarak kücükten büyüge! Basina - koyarsak büyükten kücüge siralar
        verbose_name_plural = "Ögrenciler" ## Adminde yazan Student yerine ögrenciler yazacak!

