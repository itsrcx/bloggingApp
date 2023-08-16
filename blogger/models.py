from typing import Type
from django.db import models
from django.contrib.auth.models import User
from django.db.models.options import Options
from froala_editor.fields import FroalaField
from .helpers import *
# Create your models here.



class Post(models.Model):
    status = (
    (0, "Draft"),
    (1, "Publish")
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    content = FroalaField()
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status,default = 0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = generateSlug(self.title)
        super(Post, self).save(*args, **kwargs)