from django.conf import settings
from django.db import models
from adminpanel.models import Source 

# Create your models here.
class Template(models.Model):
    name = models.CharField(max_length=100, unique=True)
    template = models.JSONField()
    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=100, unique=True)
    template = models.ForeignKey('Template', on_delete=models.CASCADE, related_name='pages')
    template_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    post_type = models.ForeignKey('PostType', on_delete=models.SET_NULL, null=True, blank=True, related_name='pages')
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True, related_name='pages') 
    def __str__(self):
        return self.name

class Taxonomy(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    post_type = models.ForeignKey('PostType', on_delete=models.CASCADE, related_name='taxonomies')

    def __str__(self):
        return self.name

class PostType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url_starter = models.SlugField(max_length=100)
    app_info = models.CharField(max_length=100 , default="pages") 
    def __str__(self):
        return self.name

class Media(models.Model):
    image_url = models.URLField()
    image_alt = models.CharField(max_length=255, blank=True)
    image_caption = models.TextField(blank=True)

    def __str__(self):
        return self.image_alt or self.image_url

class Navigation(models.Model):
    title = models.CharField(max_length=100)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True, related_name='navigation') 
    navigation_data = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
