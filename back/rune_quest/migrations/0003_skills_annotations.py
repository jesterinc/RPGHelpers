# Generated by Django 5.0.2 on 2024-03-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rune_quest', '0002_categories_charactersskills_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='annotations',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
