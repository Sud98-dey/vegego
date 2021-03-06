# Generated by Django 2.2 on 2020-10-01 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200929_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(db_column='prod_id', primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=20)),
                ('prod_price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('prod_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
