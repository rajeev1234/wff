# Generated by Django 2.0.3 on 2018-04-03 18:20

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
                ('pets_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pets_Age', models.IntegerField(default=0)),
                ('Pets_Animal_Type', models.CharField(max_length=200)),
                ('Pets_Breed', models.CharField(max_length=200)),
                ('Pets_Daily_Charges', models.IntegerField(default=0)),
                ('Pets_Description', models.CharField(max_length=500)),
                ('Pets_Ownership_Status', models.BooleanField(default=False)),
                ('Pets_Weekly_Charges', models.IntegerField(default=0)),
                ('Pets_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Pets_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='pets_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Pets'),
        ),
    ]
