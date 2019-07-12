from django.db import models


# Create your models here.
class AllMembers(models.Model):
    firstName = models.CharField(max_length=30, verbose_name="First name: ")
    secondName = models.CharField(max_length=30, verbose_name="Second name: ")
    scrumTeam = models.ForeignKey("ScrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team: ", null=True, blank=True)
    scrum_team_roles = models.ForeignKey("ScrumTeamRole", on_delete=models.CASCADE, verbose_name="Scrum Team Roles: ", null=True, blank=True)
    myskill = models.ManyToManyField('skills', blank=True, verbose_name="Skills")
    workpattern = models.ForeignKey("WorkPattern", on_delete=models.CASCADE, verbose_name="Work Pattern: ", null=True, blank=True)
    hours_per_week = models.CharField(max_length=3, verbose_name="Hours Per Week: ", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__ (self):
        return self.firstName

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class ScrumTeam(models.Model):
    teamName = models.CharField(max_length=30, verbose_name="scrum team name: ")
    team_type = models.ForeignKey("ScrumTeamType", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Team Type")
    current_focus = models.TextField(blank=True, null=True, verbose_name="Current Focus")
    scrum_master = models.ForeignKey("AllMembers", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Scrum Master")
    team_status = models.ForeignKey("ScrumTeamStatus", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Team Status")
    domain = models.ForeignKey('Domain', null=True, blank=True, on_delete=models.CASCADE, verbose_name="Domain")

    def __str__ (self):
        return self.teamName

    class Meta:
        verbose_name = 'Scrum Team'
        verbose_name_plural = 'Scrum Teams'


class AdminAccounts(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Admin Account'
        verbose_name_plural = 'Admin Accounts'

    def __str__(self):
        return self.FirstName


class Skills(models.Model):

    skill = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class ScrumTeamRole(models.Model):
    name = models.CharField(max_length=30, verbose_name="Scrum Team Role:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Scrum Team Role'
        verbose_name_plural = 'Scrum Team Roles'


class ScrumTeamType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Scrum Team Type'
        verbose_name_plural = 'Scrum Team Types'


class ScrumTeamStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Scrum Team Status'
        verbose_name_plural = 'Scrum Team Status'


class WorkPattern(models.Model):
    wrkPttrn = models.CharField(max_length=30, verbose_name="Work Pattern:")

    def __str__(self):
        return self.wrkPttrn

    class Meta:
        verbose_name = 'Work Pattern'
        verbose_name_plural = 'Work Patterns'


class Domain(models.Model):
    domain_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.domain_name

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'