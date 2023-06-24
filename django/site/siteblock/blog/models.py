from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="uel", unique=True)
    

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse ("category", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, verbose_name="uel", unique=True)


    def __str__(self) :
        return self.title
    
    class Meta:
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="uel", unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    creared_ad = models.DateTimeField(auto_now_add=True, verbose_name="опубликованна")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")


    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse ("post", kwargs={"slug": self.slug})
    

    class Meta:
        ordering = ["creared_ad"]



