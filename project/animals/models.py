from django.db import models

# Create your models here.

# class material(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     rarity = models.IntegerField(default=0)

# class furniture(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,unique=True)
#     size = models.IntegerField(default=0)
#     sold = models.IntegerField(default=-1)
#     bought = models.IntegerField(default=-1)
#     source = models.IntegerField(default=0)
#     customize = models.IntegerField(default=0)

# class recipe(models.Model):
#     id = models.AutoField(primary_key=True)
#     fid = models.IntegerField()
#     mid = models.IntegerField()
#     number = models.IntegerField(default=0)