# Generated by Django 5.0.2 on 2024-03-05 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaigns', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=30)),
                ('dies', models.JSONField(verbose_name=[{'attribute': 'str', 'dies_number': 3, 'faces': 6, 'minus': 0, 'plus': 0}, {'attribute': 'con', 'dies_number': 3, 'faces': 6, 'minus': 0, 'plus': 0}, {'attribute': 'siz', 'dies_number': 2, 'faces': 6, 'minus': 0, 'plus': 6}, {'attribute': 'int', 'dies_number': 2, 'faces': 6, 'minus': 0, 'plus': 6}, {'attribute': 'pow', 'dies_number': 3, 'faces': 6, 'minus': 0, 'plus': 0}, {'attribute': 'dex', 'dies_number': 3, 'faces': 6, 'minus': 0, 'plus': 0}, {'attribute': 'app', 'dies_number': 3, 'faces': 6, 'minus': 0, 'plus': 0}])),
                ('move_rates', models.IntegerField(default=2)),
                ('creation_points', models.IntegerField(default=300)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'rq_races',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RuneQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventurer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('homeland_clan', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.CharField(blank=True, choices=[('ply', 'player'), ('mtr', 'master'), ('bth', 'both')], max_length=3, null=True)),
                ('parent_occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('culture', models.CharField(blank=True, max_length=50, null=True)),
                ('adventurer_occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('free', models.CharField(blank=True, max_length=100, null=True)),
                ('current_str', models.IntegerField(default=8)),
                ('original_str', models.IntegerField(default=8)),
                ('current_con', models.IntegerField(default=8)),
                ('original_con', models.IntegerField(default=8)),
                ('current_siz', models.IntegerField(default=8)),
                ('original_siz', models.IntegerField(default=8)),
                ('current_int', models.IntegerField(default=8)),
                ('original_int', models.IntegerField(default=8)),
                ('current_pow', models.IntegerField(default=8)),
                ('original_pow', models.IntegerField(default=8)),
                ('current_dex', models.IntegerField(default=8)),
                ('original_dex', models.IntegerField(default=8)),
                ('current_app', models.IntegerField(default=8)),
                ('original_app', models.IntegerField(default=8)),
                ('damage_modifier', models.IntegerField(default=8)),
                ('move_rate', models.IntegerField(default=8)),
                ('dex_srm', models.IntegerField(default=8)),
                ('siz_srm', models.IntegerField(default=8)),
                ('magic_points', models.IntegerField(default=0)),
                ('fatigue_points', models.IntegerField(default=0)),
                ('hit_points', models.IntegerField(default=0)),
                ('skills', models.JSONField(blank=True, null=True, verbose_name={})),
                ('magic', models.JSONField(blank=True, null=True, verbose_name={})),
                ('weapons_skills', models.JSONField(blank=True, null=True, verbose_name={})),
                ('hit_points_locations', models.JSONField(blank=True, null=True, verbose_name={})),
                ('notes', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RuneQuest_Campaigns', to='campaigns.campaigns')),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RuneQuest_Players', to='players.players')),
            ],
            options={
                'db_table': 'rune_quest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SkillsModifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agility', models.IntegerField(default=0)),
                ('communication', models.IntegerField(default=0)),
                ('knowledge', models.IntegerField(default=0)),
                ('magical', models.IntegerField(default=0)),
                ('manipulation', models.IntegerField(default=0)),
                ('perception', models.IntegerField(default=0)),
                ('stealth', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CategoryModifiers_RuneQuest', to='rune_quest.runequest')),
            ],
            options={
                'db_table': 'rq_skills_modifiers',
                'managed': True,
            },
        ),
    ]
