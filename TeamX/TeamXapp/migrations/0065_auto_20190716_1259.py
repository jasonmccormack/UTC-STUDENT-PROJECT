# Generated by Django 2.2.3 on 2019-07-16 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0064_auto_20190716_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='leavestatus',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='scrumteamrole',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='scrumteamstatus',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='scrumteamtype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='skills',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='in_team',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=3, null=True, verbose_name='In team'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='TeamXapp.ScrumTeam', verbose_name='Scrum teams'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TeamXapp.ScrumTeamRole', verbose_name='Roles'),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='work_pattern',
            field=models.CharField(blank=True, choices=[('FULL TIME', 'Full time'), ('PART TIME', 'Part time'), ('COMPRESSED HOURS', 'Compressed hours')], default='FULL TIME', max_length=16, null=True),
        ),
    ]
