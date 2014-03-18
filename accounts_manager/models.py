from django.contrib.auth.models import AbstractUser
from django.db import models


# The main model for USERS.  Only has the basic login info.
# Information beyond this is stored in the Profiles.


class MainUser(AbstractUser):

    def is_actor(self):
        if self.actor.first_name:
            return True
        else:
            return False




# Tags, for matching actors and auditions


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


# The actor profile, containing all the basic information an actor would need to store.


class ActorProfile(models.Model):

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    headshot = models.ImageField(upload_to="headshot_pictures", blank=True)
    highlight_reel = models.FileField(upload_to="highlight_reels", blank=True)
    phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    user = models.OneToOneField(MainUser, related_name='actor')
    tag = models.ManyToManyField(Tag)
    age = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.last_name

# Same as before, but for a Production team.


class ProductionProfile(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    company_pic = models.ImageField(upload_to="company_pictures", blank=True)
    user = models.OneToOneField(MainUser, related_name='producer')

    def __unicode__(self):
        return self.name


