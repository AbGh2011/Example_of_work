# Generated by Django 5.1.3 on 2024-11-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-username']},
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['-username'], name='personal_us_usernam_774b73_idx'),
        ),
    ]
