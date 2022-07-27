from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    STATUS = (
        ('POSTED', 'POSTED'),
        ('NOT POSTED', 'NOT POSTED')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', blank=True)
    text = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=10, default="NOT POSTED")

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>No image</p>')


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name