from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Category', default='travel')
    slug = models.SlugField(max_length=200, default='')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/')
    draft = models.BooleanField(null=False, blank=True, default=True)
    pub_date = models.DateTimeField(verbose_name='Date published', null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    content = models.TextField()
    post = models.ForeignKey(Post,  on_delete=models.PROTECT, null=True)
    pub_date = models.DateTimeField(verbose_name='Created on ', null=True)
    accepted = models.BooleanField(null=False, blank=True, default=True)

    def __str__(self):
        return self.content


