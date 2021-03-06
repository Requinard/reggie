# Generated by Django 2.1.7 on 2019-03-19 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private_profile', models.BooleanField(default=False)),
                ('address_street', models.CharField(blank=True, max_length=100, null=True)),
                ('address_postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('address_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address_city', models.CharField(blank=True, max_length=30, null=True)),
                ('address_country', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.IntegerField(choices=[(0, 'Not specified'), (1, 'Male'), (2, 'Female'), (3, 'Other')], default=0)),
                ('shirt_size', models.IntegerField(blank=True, choices=[(0, 'XXS'), (1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], null=True)),
                ('profile_comments', models.TextField(blank=True, null=True)),
                ('profile_private_comments', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
