# Generated by Django 3.0.4 on 2020-03-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0002_auto_20200310_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='repository',
            name='packages_dot_json',
        ),
        migrations.AddField(
            model_name='repository',
            name='dependencies',
            field=models.ManyToManyField(blank=True, to='repositories.Dependency'),
        ),
    ]
