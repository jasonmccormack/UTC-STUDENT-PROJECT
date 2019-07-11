from django.contrib import admin
from .models import allUsers, AdminAccounts, Skills, scrumTeam

# Register your models here.
admin.site.register(allUsers)
admin.site.register(scrumTeam)
admin.site.register(AdminAccounts)
admin.site.register(Skills)