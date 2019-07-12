from django.contrib import admin
from .models import AllMembers, AdminAccounts, Skills, ScrumTeam, ScrumTeamRole, WorkPattern, ScrumTeamStatus, ScrumTeamType, Domain

# Admin
class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['first_name', 'second_name', 'scrum_team', 'skills'])
    search_fields = (['scrum_team_name', 'first_name', 'second_name'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'current_focus',])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = (['teamName', "scrum_master", "team_status", "team_type", "current_focus"])

# Register your models here.
admin.site.register(AllMembers)#, AllMemberAdmin)
admin.site.register(ScrumTeam, ScrumTeamAdmin)
admin.site.register(AdminAccounts)
admin.site.register(Skills)
admin.site.register(ScrumTeamRole)
admin.site.register(WorkPattern)
admin.site.register(ScrumTeamType)
admin.site.register(ScrumTeamStatus)
admin.site.register(Domain)
