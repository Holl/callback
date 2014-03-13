from django.contrib import admin
from accounts_manager.models import ActorProfile, ProductionProfile, Tag, MainUser


admin.site.register(MainUser)
admin.site.register(ActorProfile)
admin.site.register(ProductionProfile)
admin.site.register(Tag)