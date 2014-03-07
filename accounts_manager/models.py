from django.db import models
from registration.models import User


# The main model for USERS.  Only has the basic login info.
# Information beyond this is stored in the Profiles.


class MainUser(User):

    def is_actor(self):
        return self.actor.exists()


# Tags, for matching actors and auditions


class Tag(models.Model):
    name = models.CharField(max_length=40)


# The actor profile, containing all the basic information an actor would need to store.


class ActorProfile(models.Model):

    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Both', 'Both'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    headshot = models.ImageField(upload_to="headshot_pictures")
    highlight_reel = models.FileField(upload_to="highlight_reels")
    phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    user = models.OneToOneField(MainUser, related_name='actor')
    tag = models.ManyToManyField(Tag)
    age = models.PositiveSmallIntegerField()


# Same as before, but for a Production team.


class ProductionProfile(models.Model):
    bio = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    company_pic = models.ImageField(upload_to="company_pictures")
    user = models.OneToOneField(MainUser)


# Info stored for an individual audition.


class Audition(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="audition_pictures")
    males = models.BinaryField()
    females = models.BinaryField()
    age_range = models.CharField(max_length=20)
    num_parts = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    location_name = models.CharField(max_length=100)
    production_user = models.ForeignKey(ProductionProfile)
    actor_user = models.ManyToManyField(ActorProfile)
    tag = models.ManyToManyField(Tag)
