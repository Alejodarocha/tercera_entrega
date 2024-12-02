# Generated by Django 5.1.2 on 2024-12-02 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0002_alter_page_fecha_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='imagen',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]