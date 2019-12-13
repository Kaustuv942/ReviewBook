from django.db import models
from base.models import Genre, Star, Director, Publication

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location(instance, filename):
    file_path = 'movies/{movie_name}/{filename}'.format(
        movie_name=str(instance.name), filename=filename
    )
    return file_path

class Movie(models.Model):
    name =         models.CharField(max_length=400)
    releasedate =  models.DateField('date released')
    description =  models.TextField(blank=True)
    stars =        models.ManyToManyField(Star)
    genre =        models.ManyToManyField(Genre)
    director =     models.ForeignKey(Director, on_delete=models.CASCADE)
    runningtime =  models.DurationField()
    totalreview =  models.IntegerField(default=0)
    nor =          models.IntegerField(default=0)
    publication =  models.ForeignKey(Publication,on_delete=models.CASCADE, null=True, blank=True)
    image =        models.ImageField(upload_to=upload_location, null=False, blank=False)
    avgreview =    models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    rating = models.IntegerField()
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="Date Reviewed")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Movie)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_review_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.movie.name + "-" + instance.author.username + "-" +instance.title)

pre_save.connect(pre_save_review_receiver, sender=Review)
