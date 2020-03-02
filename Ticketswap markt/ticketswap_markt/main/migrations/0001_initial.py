# Generated by Django 2.2.10 on 2020-02-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('nr_of_tickets_bought', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
