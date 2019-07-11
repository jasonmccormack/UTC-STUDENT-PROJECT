from django.db import models

# Create your models here.
class allUsers(models.Model):
    firstName = models.CharField(max_length=30, verbose_name="First name: ")
    secondName = models.CharField(max_length=30, verbose_name="Second name: ")
    scrumTeam = models.ForeignKey("scrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team: ", null=True, blank=True)
    scrumTeamRole = models.ForeignKey("scrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team role: ", null=True, blank=True)

    def str(self):
        return self.firstName
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class scrumTeam(models.Model):
    teamName = models.CharField(max_length=30, verbose_name="scrum team name: ")
    description = models.TextField(blank=True, null=True)
    scrum_master = models.ForeignKey("Users", on_delete=models.CASCADE, null=True, blank=True)
    domain = models.ForeignKey('Domain', null=True, blank=True, on_delete=models.CASCADE)

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


class Skills(models.Model):
    
    skill = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
