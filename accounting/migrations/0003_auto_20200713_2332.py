# Generated by Django 3.0.6 on 2020-07-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20200713_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='base',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='difficulty',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='experience',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='reason',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='recommend',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
