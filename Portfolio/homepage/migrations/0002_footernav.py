# Generated by Django 3.2.11 on 2022-02-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterNav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footerheading', models.CharField(blank=True, max_length=100, null=True)),
                ('footer1', models.CharField(blank=True, max_length=100, null=True)),
                ('footer2', models.CharField(blank=True, max_length=100, null=True)),
                ('footer3', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]