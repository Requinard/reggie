# Generated by Django 2.1.7 on 2019-03-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20190313_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
