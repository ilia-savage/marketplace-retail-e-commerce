from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'