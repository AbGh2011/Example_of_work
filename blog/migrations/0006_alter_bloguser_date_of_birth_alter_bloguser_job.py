# Generated by Django 5.1.3 on 2024-11-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image_post_blog_post_publish_bb7600_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='job',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='شغل'),
        ),
    ]
