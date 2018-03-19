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
