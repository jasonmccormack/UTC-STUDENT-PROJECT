from django.contrib import admin
from .models import AllMembers, Skills, ScrumTeam, ScrumTeamRole, LeaveStatus , ScrumTeamStatus, ScrumTeamType, Domain, LeaveCalendar

# Admin
""" class AllMemberAdmin(admin.ModelAdmin):
    list_display = (['first_name', 'second_name', 'scrum_team_name', 'leave_status', 'leave_start_time', 'leave_end_time', 'leave_note'])
    search_fields = (['scrum_team_name', 'first_name', 'second_name'])
    list_filter = (['scrum_team_name', 'leave_status']) """

class TeamAdmin(admin.ModelAdmin):
    list_display = (['name', 'scrum_master', 'status', 'current_focus',])

class ScrumTeamAdmin(admin.ModelAdmin):
    list_display = (['teamName', "scrum_master", "team_status", "team_type", "current_focus", "domain"])
    list_filter = (['domain'])

# Register your models here.
admin.site.register(AllMembers)
admin.site.register(ScrumTeam, ScrumTeamAdmin)
admin.site.register(Skills)
admin.site.register(ScrumTeamRole)
admin.site.register(ScrumTeamType)
admin.site.register(ScrumTeamStatus)
admin.site.register(Domain)
admin.site.register(LeaveStatus)
admin.site.register(LeaveCalendar)

