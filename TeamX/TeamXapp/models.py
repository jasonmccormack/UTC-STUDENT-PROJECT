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
    teamName = CharField(max_length=30, verbose_name="scrum team name: ")