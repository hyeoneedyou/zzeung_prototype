# Generated by Django 3.0.6 on 2020-07-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('reason', models.TextField()),
                ('base', models.TextField()),
                ('experience', models.TextField()),
                ('difficulty', models.TextField()),
                ('recommend', models.TextField()),
                ('content', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
