# Generated by Django 2.1 on 2018-01-08 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bugcontext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_title', models.CharField(max_length=100)),
                ('bug_level', models.CharField(max_length=4)),
                ('bug_body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('bug_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
