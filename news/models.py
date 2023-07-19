from django.db import models

import datetime
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    full = models.TextField()
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name="News"
        verbose_name_plural="News"

    def __str__(self):
        return self.title