from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class PublishedManager(models.Manager):
    
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset()\
                        .filter(status='published')


class Post(models.Model):
    status_choices = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                               choices=status_choices,
                               default='draft')

    #objects = models.Manager()  # default manager
    published =PublishedManager()   #custom manager

    def get_absolute_url(self):
        return reverse('advblog:post_detail',
                        args = [ self.publish.year,
                                self.publish.month,
                                self.publish.day,
                                self.slug])

    

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    
