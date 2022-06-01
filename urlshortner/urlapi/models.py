from django.db import models

# Create your models here.
class URLShortner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=False)

    def __str__(self):
        return self.short_url

    
