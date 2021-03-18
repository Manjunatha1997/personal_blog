from django.db import models

# Create your models here.


class Info(models.Model):
    about = models.CharField(max_length=10000)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=1000)
    language = models.CharField(max_length=1000)


class Experience(models.Model):
    title_or_designation = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=100)


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency = models.IntegerField()


