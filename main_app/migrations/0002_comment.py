# Generated by Django 4.2.8 on 2024-01-02 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comments', models.CharField(max_length=100)),
                ('potato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.potato')),
            ],
        ),
    ]
