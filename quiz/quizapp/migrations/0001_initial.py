# Generated by Django 3.2.8 on 2022-01-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('batafsil', models.CharField(blank=True, max_length=200)),
                ('savol_son', models.PositiveSmallIntegerField()),
                ('davomiyligi', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Savol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizapp.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Javob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('togri', models.BooleanField(default=False)),
                ('savol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizapp.savol')),
            ],
        ),
    ]