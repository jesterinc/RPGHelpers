# Generated by Django 5.0.2 on 2024-03-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0002_remove_historicaltokens_campaign_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltokens',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tokens',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
