# Generated by Django 5.0.2 on 2024-03-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rune_quest', '0006_rename_charactersskills_characterskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_skill', models.IntegerField(default=0)),
                ('critical_success', models.IntegerField(default=0)),
                ('special_success', models.IntegerField(default=0)),
                ('fumble', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'rq_skill_result',
                'managed': True,
            },
        ),
    ]
