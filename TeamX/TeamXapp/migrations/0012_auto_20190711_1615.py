# Generated by Django 2.2.3 on 2019-07-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0011_auto_20190711_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumteam',
            name='description',
        ),
        migrations.AddField(
            model_name='scrumteam',
            name='current_focus',
            field=models.TextField(blank=True, null=True, verbose_name='Current Focus'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrumTeam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeam', verbose_name='Scrum team: '),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeamRole', verbose_name='Scrum Team Roles: '),
        ),
    ]
