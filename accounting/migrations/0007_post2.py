# Generated by Django 3.0.6 on 2020-07-27 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0006_auto_20200727_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('reason', models.TextField(null=True)),
                ('base', models.TextField(null=True)),
                ('experience', models.TextField(null=True)),
                ('difficulty', models.TextField(null=True)),
                ('recommend', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('view_count', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
