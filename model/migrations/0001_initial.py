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
                ('Model_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Models_Body_Type', models.CharField(max_length=200)),
                ('Models_Description', models.CharField(max_length=200)),
                ('Models_Ethnicity', models.CharField(max_length=200)),
                ('Models_Eye_Colour', models.CharField(max_length=200)),
                ('Models_Hair_Colour', models.CharField(max_length=200)),
                ('Models_Height', models.CharField(max_length=100)),
                ('Models_Scene_Comfort', models.CharField(max_length=200)),
                ('Models_Skin_Color', models.CharField(max_length=200)),
                ('Models_Smoker', models.CharField(max_length=100)),
                ('Models_Special_Skills', models.CharField(max_length=200)),
                ('Models_Weight', models.CharField(max_length=100)),
                ('Models_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Models_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Model_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='model.Models'),
        ),
    ]
