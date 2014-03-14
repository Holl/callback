from django.db import models
from accounts_manager.models import ProductionProfile, ActorProfile, Tag


class Audition(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="audition_pictures", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    location_name = models.CharField(max_length=100)
    audition_date = models.DateTimeField(null=True, blank=True)
    production_user = models.ForeignKey(ProductionProfile)
    actor_user = models.ManyToManyField(ActorProfile, null=True)
    tag = models.ManyToManyField(Tag)

    def total_parts(self):
        return len()


class Part(models.Model):

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    gender = models.CharField(max_length=1, choices=GENDER)
    age_range = models.CharField(max_length=10)
    audition = models.ForeignKey(Audition)
