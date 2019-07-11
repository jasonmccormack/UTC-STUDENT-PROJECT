from django.contrib import admin
from .models import allUsers, AdminAccounts, Skills, scrumTeam

# Admin 
class UserAdmin(admin.ModelAdmin):
    list_display = (['FirstName', 'LastName', 'ScrumTeams', 'Skills'])
    search_fields = (['scrum_team_name', 'first_name', 'surname'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'description'])

# Register your models here.
admin.site.register(allUsers)
admin.site.register(scrumTeam)
admin.site.register(AdminAccounts)
admin.site.register(Skills)