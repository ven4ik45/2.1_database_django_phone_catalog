from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField(max_length=250)
    # release_date = models.CharField(max_length=12)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
