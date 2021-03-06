# Generated by Django 3.1.6 on 2021-04-17 16:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('games_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=400)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('to_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_app.game')),
            ],
        ),
    ]
