# Generated by Django 3.2.13 on 2022-10-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslık', models.CharField(max_length=100, verbose_name='İçerik Başlığı')),
                ('yazi', models.CharField(max_length=1000, verbose_name='İçerik Yazısı')),
                ('resim', models.FileField(blank=True, null=True, upload_to='filmResmi/', verbose_name='Film Resmi')),
            ],
        ),
    ]
