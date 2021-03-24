# Generated by Django 3.1.4 on 2021-01-03 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpanel', '0005_auto_20201228_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.CharField(default=uuid.UUID('6853c9c9-58b4-4375-8135-da6130e4a2b8'), max_length=256, primary_key=True, serialize=False)),
                ('teamCode', models.CharField(max_length=256)),
                ('createdBy', models.CharField(max_length=256)),
                ('teamName', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='submission',
            name='questionId',
        ),
        migrations.AddField(
            model_name='submission',
            name='checkedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='submission',
            name='checkedOrNot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='points',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='submission',
            name='roundId',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.round'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='components',
            name='id',
            field=models.CharField(default=uuid.UUID('b03a2482-e6db-4f2b-878f-e7a22717e848'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contest',
            name='id',
            field=models.CharField(default=uuid.UUID('b6b11170-05f5-4515-b508-49d9de327466'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.CharField(default=uuid.UUID('94994076-08f5-47e5-aaee-e44d2f0a80dd'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='round',
            name='id',
            field=models.CharField(default=uuid.UUID('0857f584-2b6b-4c62-b296-d27dd92e86c4'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.CharField(default=uuid.UUID('8d9ff555-fbe8-4f2b-95fb-27aa5c173e3a'), max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='teamCode',
            field=models.ForeignKey(default='e7a3e087-4e35-4315-a57c-06d3cc0a8145', on_delete=django.db.models.deletion.PROTECT, to='adminpanel.team'),
            preserve_default=False,
        ),
    ]