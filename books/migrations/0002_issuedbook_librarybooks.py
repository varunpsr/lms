# Generated by Django 2.2.6 on 2019-10-17 04:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20191017_0942'),
        ('accounts', '0002_auto_20191016_1905'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('ON_LOAN', 'On Loan'), ('BOOKED', 'Booked')], default='AL', max_length=2, verbose_name='Status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library', verbose_name='Library')),
            ],
            options={
                'verbose_name': 'Library Books',
                'verbose_name_plural': 'Library Books',
            },
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField(auto_now_add=True, verbose_name='Date of Issue')),
                ('date_of_return', models.DateField(default=datetime.date(2019, 10, 24), verbose_name='Date of Return')),
                ('actual_date_of_return', models.DateField(blank=True, null=True, verbose_name='Actual Date of Return')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.Book', verbose_name='Book')),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Librarian', verbose_name='Librarian')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library', verbose_name='Library')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Member', verbose_name='Member')),
            ],
            options={
                'verbose_name': 'Issued Book',
                'verbose_name_plural': 'Issued Books',
            },
        ),
    ]
