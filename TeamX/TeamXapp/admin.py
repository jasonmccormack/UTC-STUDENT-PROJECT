from django.contrib import admin
from .models import allUsers, adminAccounts, skills, scrumTeam, scrumTeamRole, Work_Pattern

# Admin 
class allUserAdmin(admin.ModelAdmin):
    list_display = (['firstName', 'secondName', 'scrumTeam', 'skills'])
    search_fields = (['scrum_team_name', 'first_name', 'surname'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'description'])

# Register your models here.
admin.site.register(allUsers)#, allUserAdmin)
admin.site.register(scrumTeam)
admin.site.register(adminAccounts)
admin.site.register(skills)
admin.site.register(scrumTeamRole) 
admin.site.register(Work_Pattern)