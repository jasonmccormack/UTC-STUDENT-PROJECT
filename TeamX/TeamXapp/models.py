from django.db import models

# Create your models here.
class AllMembers(models.Model):
    firstName = models.CharField(max_length=30, verbose_name="First name: ")
    secondName = models.CharField(max_length=30, verbose_name="Second name: ") 
    scrumTeam = models.ForeignKey("scrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team: ", null=True, blank=True)
    myskill = models.ManyToManyField('skills', blank=True)
    WorkPattern = models.ForeignKey("Work_pattern", on_delete=models.CASCADE, verbose_name="Work Pattern: ", null=True, blank=True)
    Hours_Per_Week = models.CharField(max_length=30, verbose_name="Hours Per Week: ", null=True, blank=True)


    def __str__ (self):
        return self.firstName

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class ScrumTeam(models.Model):
    teamName = models.CharField(max_length=30, verbose_name="scrum team name: ")
    description = models.TextField(blank=True, null=True)
    scrum_master = models.ForeignKey("AllMembers", on_delete=models.CASCADE, null=True, blank=True)
    #domain = models.ForeignKey('Domain', null=True, blank=True, on_delete=models.CASCADE)

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

class Work_Pattern(models.Model):
    WrkPttrn = models.CharField(max_length=30, verbose_name="Work Pattern:")

    def __str__(self):
        return self.WrkPttrn

    class Meta:
        verbose_name = 'Work Pattern'
        verbose_name_plural = 'Work Patterns'