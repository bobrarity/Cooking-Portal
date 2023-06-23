# Generated by Django 4.0.5 on 2022-09-10 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_site', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField()),
                ('bio', models.TextField()),
                ('website', models.TextField()),
                ('twitter', models.TextField()),
                ('instagram', models.TextField()),
                ('facebook', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
