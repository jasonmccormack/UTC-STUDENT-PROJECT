from django.contrib import admin
from .models import AllMembers, AdminAccounts, Skills, ScrumTeam, ScrumTeamRole, WorkPattern, ScrumTeamStatus, ScrumTeamType

# Admin 
class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['firstName', 'secondName', 'scrumTeam', 'skills'])
    search_fields = (['scrum_team_name', 'first_name', 'surname'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'current_focus',])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = ([''])

# Register your models here.
admin.site.register(AllMembers)#, allUserAdmin)
admin.site.register(ScrumTeam)
admin.site.register(AdminAccounts)
admin.site.register(Skills)
admin.site.register(ScrumTeamRole) 
admin.site.register(WorkPattern)
admin.site.register(ScrumTeamType)
admin.site.register(ScrumTeamStatus)
