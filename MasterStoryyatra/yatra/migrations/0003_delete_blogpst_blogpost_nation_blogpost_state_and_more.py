# Generated by Django 4.1.7 on 2023-03-30 17:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yatra', '0002_blogpst'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPst',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Nation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
