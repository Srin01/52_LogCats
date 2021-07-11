# Generated by Django 3.0.5 on 2021-07-10 15:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0013_auto_20210710_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 15, 14, 8, 9093, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='SellerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(max_length=15, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('contactNo', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IsLocalGrocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOwner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
