from django.contrib import admin
from .models import AllMembers, Skills, ScrumTeam, ScrumTeamRole, LeaveStatus , ScrumTeamStatus, ScrumTeamType, Domain, LeaveCalendar, JobRoleGroup

# Admin
class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['first_name', 'second_name', 'scrum_team_name', 'work_pattern'])
    search_fields = (['scrum_team_name', 'first_name', 'second_name'])
    list_filter = (['scrum_team_name'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'current_focus',])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = (['team_name', "scrum_master", "team_status", "team_type", "current_focus", "domain"])
    list_filter = (['domain'])

class ScrumTeamRoleAdmin(admin.ModelAdmin):
    list_display = (["name", "job_role_group"])
    list_filter = (["job_role_group"])

# Register your models here.
admin.site.register(AllMembers, AllMemberAdmin)
admin.site.register(ScrumTeam, ScrumTeamAdmin)
admin.site.register(Skills)
admin.site.register(ScrumTeamRole, ScrumTeamRoleAdmin)
admin.site.register(ScrumTeamType)
admin.site.register(ScrumTeamStatus)
admin.site.register(Domain)
admin.site.register(LeaveStatus)
admin.site.register(LeaveCalendar)
admin.site.register(JobRoleGroup)

