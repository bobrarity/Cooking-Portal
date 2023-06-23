from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Category title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Recipe title')
    content = models.TextField(default='Recipe description coming soon', verbose_name='Recipe text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Image')
    watched = models.IntegerField(default=0, verbose_name='Views')
    is_published = models.BooleanField(default=True, verbose_name='Is published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    author = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    mobile = models.CharField(max_length=80, blank=True, null=True)
    website = models.CharField(max_length=20, blank=True, null=True)
    github = models.CharField(max_length=20, blank=True, null=True)
    twitter = models.CharField(max_length=20, blank=True, null=True)
    instagram = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
