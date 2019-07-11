# Generated by Django 2.2.3 on 2019-07-11 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0013_auto_20190711_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domain',
            options={'verbose_name': 'Domain', 'verbose_name_plural': 'Domains'},
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
        migrations.AlterField(
            model_name='scrumteam',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.Domain', verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='scrumteam',
            name='scrum_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.AllMembers', verbose_name='Scrum Master'),
        ),
        migrations.AlterField(
            model_name='scrumteam',
            name='team_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeamStatus', verbose_name='Team Status'),
        ),
        migrations.AlterField(
            model_name='scrumteam',
            name='team_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeamType', verbose_name='Team Type'),
        ),
    ]
