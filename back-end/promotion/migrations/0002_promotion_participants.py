# Generated by Django 3.1.7 on 2021-03-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='participants',
            field=models.ManyToManyField(to='promotion.Seller'),
        ),
    ]
