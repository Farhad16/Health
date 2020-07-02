# Generated by Django 3.0.7 on 2020-06-20 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200615_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('register_no', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='systemuser',
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
        migrations.AddField(
            model_name='nurse',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Hospital'),
        ),
    ]