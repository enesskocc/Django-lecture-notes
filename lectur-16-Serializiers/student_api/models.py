from django.db import models



class Path(models.Model):
    path_name= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"



class Student(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
 # blank=True for admin dashboard
 # null=True for db
    def __str__(self):
        return f"{self.last_name} {self.first_name}"



    