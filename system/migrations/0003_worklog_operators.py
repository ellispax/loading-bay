# Generated by Django 4.1.5 on 2024-01-20 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0002_alter_dieselpurchase_supplier_otherexpenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('openingHr', models.DecimalField(decimal_places=2, max_digits=20)),
                ('closingHr', models.DecimalField(decimal_places=2, max_digits=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('start_diesel', models.IntegerField()),
                ('end_diesel', models.IntegerField(blank=True, null=True)),
                ('Fuel', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amnt_earned', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_machine_name', to='system.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mch_op_name', to='system.equipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opr_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
