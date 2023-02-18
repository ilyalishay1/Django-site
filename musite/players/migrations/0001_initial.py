# Generated by Django 4.1.5 on 2023-01-23 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlayersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.category')),
            ],
        ),
    ]