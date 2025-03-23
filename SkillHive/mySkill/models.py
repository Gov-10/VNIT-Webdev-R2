from django.db import models
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Make name unique for slug generation
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
    description = models.TextField()
    fee = models.IntegerField(default=0)
    duration = models.IntegerField(default=1)  # Duration in years
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Event.objects.filter(slug=slug).exists():  # Ensure uniqueness
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    
