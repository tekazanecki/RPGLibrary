from django.db import models

# Create your models here.
from django.db import models

class Setting(models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(null=True,  blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    src_link = models.URLField(null=True, blank=True)
    img_link = models.URLField(null=True, blank=True)
    setting = models.ForeignKey(Setting, related_name='books', on_delete=models.CASCADE, null=True,  blank=True)

    def __str__(self):
        return self.title