from django.db import models

# Create your models here.
class allUsers(models.Model):
    firstName = CharField(max_length=30, verbose_name="First name: ")
    secondName = CharField(max_length=30, verbose_name="Second name: ")
    scrumTeam = ForeignKey("scrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team: ", null=True, blank=True)
    scrumTeamRole = ForeignKey("scrumTeam", on_delete=models.CASCADE, verbose_name="Scrum team role: ", null=True, blank=True)

    def str(self):
        return self.firstName
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class scrumTeam(models.Model):
    teamName = CharField(max_length=30, verbose_name="scrum team name: ")