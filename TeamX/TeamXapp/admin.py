from django.contrib import admin
from .models import Users, AdminAccounts, Skills, ScrumTeams

# Register your models here.
admin.site.register(Users)
admin.site.register(ScrumTeams)
admin.site.register(AdminAccounts)
admin.site.register(Skills)