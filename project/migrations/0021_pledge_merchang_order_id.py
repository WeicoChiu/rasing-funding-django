# Generated by Django 3.2.5 on 2021-11-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_alter_pledge_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='merchang_order_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
