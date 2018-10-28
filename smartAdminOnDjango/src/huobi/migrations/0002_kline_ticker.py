# Generated by Django 2.1.2 on 2018-10-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huobi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('amount', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('count', models.IntegerField()),
                ('open', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('vol', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('amount', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('count', models.IntegerField()),
                ('open', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('vol', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
            ],
        ),
    ]