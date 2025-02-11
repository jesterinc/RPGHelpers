# Generated by Django 5.0.2 on 2024-03-07 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rune_quest', '0009_skills_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_value', models.IntegerField(default=0)),
                ('ceremony', models.IntegerField(default=0)),
                ('enchant', models.IntegerField(default=0)),
                ('summon', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('intensity', models.IntegerField(default=0)),
                ('multispell', models.IntegerField(default=0)),
                ('spell_range', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Magic_RuneQuest', to='rune_quest.runequest')),
            ],
            options={
                'db_table': 'rq_magic',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MagicSpells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('checked', models.BooleanField(default=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MagicSpells_RuneQuest', to='rune_quest.runequest')),
            ],
            options={
                'db_table': 'rq_magic_spells',
                'managed': True,
            },
        ),
    ]
