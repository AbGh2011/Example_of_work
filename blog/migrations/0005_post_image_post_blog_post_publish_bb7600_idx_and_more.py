# Generated by Django 5.1.3 on 2024-11-11 13:39

import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_author_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(max_length=250, verbose_name='اسلاگ')),
                ('publish', django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'در صف بررسی'), ('PB', 'منتشر شده'), ('RJ', 'رد شده')], default='DF', max_length=2, verbose_name='وضعیت')),
                ('reading_time', models.PositiveIntegerField(default=0, verbose_name='زمان مطالعه')),
                ('category', models.CharField(choices=[('تکنولوژی', 'تکنولوژی'), ('زبان برنامه نویسی', 'زبان برنامه نویسی'), ('هوش مصنوعی', 'هوش مصنوعی'), ('بلاکچین', 'بلاکچین'), ('سایر', 'سایر')], default='سایر', max_length=20, verbose_name='دسته بندی')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='blog.bloguser', verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=75, scale=None, size=[500, 500], upload_to='post_images/')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصویر ها',
                'ordering': ['created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['created'], name='blog_image_created_1ba45b_idx'),
        ),
    ]