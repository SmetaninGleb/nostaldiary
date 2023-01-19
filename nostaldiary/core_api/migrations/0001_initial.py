# Generated by Django 4.1.5 on 2023-01-19 17:42

import core_api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploaded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=core_api.models.image_directory_path)),
                ('user_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_images', related_query_name='user_owner', to=settings.AUTH_USER_MODEL)),
                ('users_allowed', models.ManyToManyField(related_name='accessed_images', related_query_name='users_allowed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('images_attached', models.ManyToManyField(to='core_api.imageuploaded')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_posts', related_query_name='user_creator', to=settings.AUTH_USER_MODEL)),
                ('users_allowed', models.ManyToManyField(related_name='accessed_posts', related_query_name='users_allowed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
