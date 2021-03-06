# Generated by Django 2.0.5 on 2018-05-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField(default='[]')),
            ],
            options={
                'db_table': 'result',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('frequency', models.CharField(max_length=5, unique=True)),
                ('status', models.CharField(choices=[('stoped', 'stoped'), ('running', 'running')], default='stoped', max_length=20)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=255)),
                ('task_type', models.CharField(max_length=10)),
                ('monitors', models.TextField()),
                ('task_name', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=5)),
                ('retry', models.IntegerField()),
                ('is_agent', models.BooleanField(default=False)),
                ('submit_method', models.CharField(max_length=10)),
                ('header', models.TextField(blank=True, null=True)),
                ('redirect', models.BooleanField(default=False)),
                ('time_out', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('rp_time', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['frequency'], name='frequency_idx'),
        ),
    ]
