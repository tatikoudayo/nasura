# Generated by Django 3.0.7 on 2020-06-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('money', models.IntegerField(verbose_name='価格')),
            ],
        ),
    ]
