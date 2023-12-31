# Generated by Django 4.2.6 on 2023-10-31 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'db_table': 'inventory',
                'indexes': [models.Index(fields=['user'], name='user_idx'), models.Index(fields=['product'], name='product_idx')],
            },
        ),
    ]
