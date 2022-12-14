# Generated by Django 4.0.5 on 2022-07-04 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('video_url', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=10)),
                ('height', models.IntegerField()),
                ('subs_count', models.IntegerField()),
                ('is_featured', models.BooleanField(default=False)),
                ('crew', models.CharField(choices=[('Solo', 'solo'), ('small_team', 'SM'), ('large_team', 'LM')], max_length=100)),
                ('camera_type', models.CharField(choices=[('sony', 'sony'), ('fuji', 'fuji'), ('canon', 'canon')], max_length=100)),
                ('category', models.CharField(choices=[('cooking', 'cook'), ('tech', 'tech'), ('educational', 'edu'), ('vlog', 'vlog')], max_length=100)),
                ('photo', models.ImageField(upload_to='media/youtubers/%Y/%M/%D')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
