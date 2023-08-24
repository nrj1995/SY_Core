# Generated by Django 4.1.7 on 2023-03-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='blog_photos/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='blog_photos/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='blog_photos/')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
