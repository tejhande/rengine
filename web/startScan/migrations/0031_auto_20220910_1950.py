# Generated by Django 3.2.4 on 2022-09-10 18:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0030_auto_20220718_1830'),
    ]

    operations = [
        # IpAddress
        migrations.AddField(
            model_name='ipaddress',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='reverse_pointer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='version',
            field=models.IntegerField(blank=True, null=True),
        ),

        # ScanHistory
        migrations.RemoveField(
            model_name='scanhistory',
            name='dir_file_fuzz',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='fetch_url',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='osint',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='port_scan',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='screenshot',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='subdomain_discovery',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='vulnerability_scan',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='waf_detection',
        ),

        migrations.AddField(
            model_name='scanhistory',
            name='tasks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
        migrations.AddField(
            model_name='scanhistory',
            name='celery_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='scan_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.scanhistory'),
        ),
        migrations.AlterField(
            model_name='scanhistory',
            name='scan_status',
            field=models.IntegerField(choices=[(-1, -1), (0, 0), (1, 1), (2, 2), (3, 3)], default=-1),
        ),

        # SubScan
        migrations.RemoveField(
            model_name='subscan',
            name='dir_file_fuzz',
        ),
        migrations.RemoveField(
            model_name='subscan',
            name='fetch_url',
        ),
        migrations.RemoveField(
            model_name='subscan',
            name='osint',
        ),
        migrations.RemoveField(
            model_name='subscan',
            name='port_scan',
        ),
        migrations.RemoveField(
            model_name='subscan',
            name='vulnerability_scan',
        ),
        migrations.AddField(
            model_name='subscan',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscan',
            name='celery_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),

        # ScanActivity
        migrations.AddField(
            model_name='scanactivity',
            name='name',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scanactivity',
            name='traceback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
