# Generated by Django 2.2.2 on 2019-06-10 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=200)),
                ('date_time_added', models.DateTimeField(default=datetime.date.today)),
                ('expiry_date', models.DateField()),
            ],
        ),
    ]
