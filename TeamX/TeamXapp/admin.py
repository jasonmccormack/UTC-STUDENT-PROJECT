from django.contrib import admin
from .models import AllMembers, AdminAccounts, Skills, ScrumTeam, ScrumTeamRole, WorkPattern

# Admin
class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['firstName', 'secondName', 'scrumTeam', 'skills'])
    search_fields = (['scrum_team_name', 'first_name', 'surname'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'description'])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = (['teamName', "scrum_master"])

# Register your models here.
admin.site.register(AllMembers)#, allUserAdmin)
admin.site.register(ScrumTeam, ScrumTeamAdmin)
admin.site.register(AdminAccounts)
admin.site.register(Skills)
admin.site.register(ScrumTeamRole)
admin.site.register(WorkPattern)
