# Generated by Django 2.1.7 on 2019-03-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('payed', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('reminder', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('current_date', models.DateField()),
                ('estimate_date', models.DateField()),
            ],
        ),
    ]
