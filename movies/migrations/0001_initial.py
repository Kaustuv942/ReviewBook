# Generated by Django 3.0 on 2019-12-11 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=400)),
                ('movie_date', models.DateField(verbose_name='date released')),
                ('movie_description', models.TextField(blank=True)),
                ('movie_runningtime', models.DurationField()),
                ('movie_totalreview', models.IntegerField(default=0)),
                ('movie_nor', models.IntegerField(default=0)),
                ('movie_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='movies/')),
                ('movie_avgreview', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('movie_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Director')),
                ('movie_genre', models.ManyToManyField(to='base.Genre')),
                ('movie_publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Publication')),
                ('movie_star', models.ManyToManyField(to='base.Star')),
            ],
        ),
    ]
