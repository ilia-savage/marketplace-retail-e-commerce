from django.db import models

# Create your models here.


from django.db import models
from user.models import User

class Visit(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField()
    url = models.URLField()
    os = models.CharField(max_length=200)
    browser = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user} visited {self.url} at {self.date}"