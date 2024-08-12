# Generated by Django 5.0.6 on 2024-06-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('screen_size', models.DecimalField(decimal_places=2, max_digits=3)),
                ('projector', models.DecimalField(decimal_places=2, max_digits=3)),
                ('audio', models.DecimalField(decimal_places=2, max_digits=3)),
                ('seats', models.DecimalField(decimal_places=2, max_digits=3)),
                ('surroundings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('travel', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=3)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
