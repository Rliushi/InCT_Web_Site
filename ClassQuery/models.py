from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class ClassImage(models.Model):
    classID = models.IntegerField()
    className = models.CharField(max_length=20)
    sectionID = models.IntegerField()
    imageSeq = models.IntegerField()
    imagePath = models.CharField(max_length=100)


@python_2_unicode_compatible
class XjhInfo(models.Model):
    city = models.CharField(max_length=20)
    city_id = models.CharField(max_length=10, default='xj')
    school = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=14)
