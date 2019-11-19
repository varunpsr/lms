# Generated by Django 2.2.6 on 2019-10-16 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='summary')),
                ('isbn', models.CharField(max_length=13, verbose_name='isbn')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author', verbose_name='Author')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Language', verbose_name='Language')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publication', verbose_name='Publication')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]