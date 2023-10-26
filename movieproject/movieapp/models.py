from django.db import models


# Create your models here.
class movie(models.Model):
    mname = models.CharField(max_length=250)
    mdesc = models.TextField()
    myear = models.IntegerField()
    mimg = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.mname
