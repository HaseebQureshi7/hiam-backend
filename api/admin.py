from django.contrib import admin
from .models import UserProfile, UserExperience, UserProject, UserSkill, UserCertificate, UserLink
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserExperience)
admin.site.register(UserProject)
admin.site.register(UserSkill)
admin.site.register(UserCertificate)
admin.site.register(UserLink)