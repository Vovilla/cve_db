# Generated by Django 4.1.3 on 2022-11-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cve',
            name='id',
        ),
        migrations.AlterField(
            model_name='cve',
            name='name',
            field=models.CharField(default='CVE', max_length=200, primary_key=True, serialize=False),
        ),
    ]
