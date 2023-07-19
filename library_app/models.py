from django.db import models

class RPGSetting(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rpg_settings/')

    class Meta:
        verbose_name = "RPG Setting"
        verbose_name_plural = "RPG Settings"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/')
    pdf = models.FileField(upload_to='books/pdfs/')
    rpg_setting = models.ForeignKey(RPGSetting, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title

