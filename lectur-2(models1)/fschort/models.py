import numbers
from tabnanny import verbose
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    about = models.TextField()
    register_date = models.DateField(auto_now_add=True) ## ilk basta create ettigim zamani aliyor!
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    # def __str__(self):
    #     return f"{self.number} - {self.firt_name}"

    def __str__(self):
        return f"{self.number} - {self.first_name}"

    class Meta : ## Class ile ilgili bazi ayarlamalari yapmak icin!
        ordering = ["number"]
        verbose_name_plural ="Student_List" ### tablonun ismini degistirme

     
