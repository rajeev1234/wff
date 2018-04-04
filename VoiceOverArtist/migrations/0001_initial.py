# Generated by Django 2.0.3 on 2018-04-03 11:57

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoiceOverArtist_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceOverArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoiceOverArtist_Voice_Over_Artist', models.CharField(max_length=200)),
                ('VoiceOverArtist_Charges_Available', models.BooleanField(max_length=200)),
                ('VoiceOverArtist_Daily_Charges', models.IntegerField(default=-1)),
                ('VoiceOverArtist_Description', models.CharField(max_length=200)),
                ('VoiceOverArtist_Language', models.CharField(max_length=200)),
                ('VoiceOverArtist_Voice_Over_Artist_ID', models.IntegerField(default=-1)),
                ('VoiceOverArtist_Voice_Scale', models.CharField(max_length=200)),
                ('VoiceOverArtist_Voice_Over_Artist_Message', models.CharField(max_length=280)),
                ('VoiceOverArtist_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_VoiceOverArtist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voiceoverartist', to='VoiceOverArtist.VoiceOverArtist'),
        ),
        migrations.AddField(
            model_name='comment',
            name='VoiceOverArtist_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voiceoverartist_Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
