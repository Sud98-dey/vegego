# Generated by Django 2.2 on 2020-10-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201005_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_mode',
            name='Payment_Mode',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
