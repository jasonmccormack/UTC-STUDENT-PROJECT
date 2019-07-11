# Generated by Django 2.2.3 on 2019-07-11 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0004_auto_20190711_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, verbose_name='First name: ')),
                ('secondName', models.CharField(max_length=30, verbose_name='Second name: ')),
                ('Hours_Per_Week', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hours Per Week: ')),
                ('WorkPattern', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.Work_Pattern', verbose_name='Work Pattern: ')),
                ('myskill', models.ManyToManyField(blank=True, to='TeamXapp.Skills')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AlterField(
            model_name='scrumteam',
            name='scrum_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.AllMembers'),
        ),
        migrations.DeleteModel(
            name='allUsers',
        ),
        migrations.AddField(
            model_name='allmembers',
            name='scrumTeam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeam', verbose_name='Scrum team: '),
        ),
    ]
