from django.contrib import admin
from .models import AllMembers, Skills, ScrumTeam, ScrumTeamRole, LeaveStatus , ScrumTeamStatus, ScrumTeamType, Domain, LeaveCalendar, JobRoleGroup

# Admin
class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['first_name', 'second_name', 'scrum_team_name', 'work_pattern'])
    search_fields = (['scrum_team_name', 'first_name', 'second_name'])
    list_filter = (['scrum_team_name', 'in_team', 'scrum_team_roles', 'work_pattern'])

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'current_focus',])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = (['team_name', "scrum_master", "team_status", "team_type", "current_focus", "domain"])
    list_filter = (['domain'])

class ScrumTeamRoleAdmin(admin.ModelAdmin):
    list_display = (["name", "job_role_group", "description"])
    list_filter = (["job_role_group"])

class DomainAdmin(admin.ModelAdmin):
    list_display = (["domain_name", "description"])

class SkillsAdmin(admin.ModelAdmin):
    list_display = (["skill", "description"])

class ScrumTeamTypeAdmin(admin.ModelAdmin):
    list_display = (["name", "description"])

class ScrumTeamStatusAdmin(admin.ModelAdmin):
    list_display = (["name", "description"])


# Register your models here.
admin.site.register(AllMembers, AllMemberAdmin)
admin.site.register(ScrumTeam, ScrumTeamAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(ScrumTeamRole, ScrumTeamRoleAdmin)
admin.site.register(ScrumTeamType, ScrumTeamTypeAdmin)
admin.site.register(ScrumTeamStatus, ScrumTeamStatusAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(LeaveStatus)
admin.site.register(LeaveCalendar)
admin.site.register(JobRoleGroup)
