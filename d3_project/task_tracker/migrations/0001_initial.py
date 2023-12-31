# Generated by Django 4.2.8 on 2023-12-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('estimate', models.IntegerField()),
                ('state', models.CharField(choices=[('Planned', 'Planned'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Planned', max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
    ]
