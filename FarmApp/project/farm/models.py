from django.db import models

# Create your models here.

class AnimalType(models.Model):
     name=models.CharField(max_length=50)

     def __str__(self):
        return self.name


class Feed(models.Model):
      name=models.CharField(max_length=100)
      amount=models.DecimalField(max_digits=10,decimal_places=2, default=0.0)

      def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    feeds = models.ManyToManyField(Feed)
    weight=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name




