# Generated by Django 3.1.3 on 2020-11-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_personal_portfolio', '0003_remove_people_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='last_login',
            field=models.TextField(null=True),
        ),
    ]