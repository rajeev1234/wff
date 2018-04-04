# Generated by Django 2.0.3 on 2018-04-03 12:14

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
                ('Singer_Comment', models.CharField(max_length=150)),
                ('Singer_Comment_Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Singer_Daily_Charges', models.IntegerField()),
                ('Singer_Description', models.CharField(max_length=200)),
                ('Singer_Financials_Available', models.BooleanField(max_length=200)),
                ('Singer_Genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsSinger', to='Singer.Singer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Singer_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssSinger', to=settings.AUTH_USER_MODEL),
        ),
    ]
