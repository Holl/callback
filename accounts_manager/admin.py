from django.contrib import admin
from accounts_manager.models import ActorProfile, ProductionProfile, Audition, Tag, MainUser
# Register your models here.

admin.site.register(MainUser)
admin.site.register(ActorProfile)
admin.site.register(ProductionProfile)
admin.site.register(Audition)
admin.site.register(Tag)