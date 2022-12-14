# Generated by Django 3.2 on 2022-11-06 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Раздел')),
                ('description', models.TextField(blank=True, verbose_name='Описание раздела')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='разновидность')),
            ],
        ),
        migrations.CreateModel(
            name='SizeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(verbose_name='Длинна')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('thickness', models.FloatField(verbose_name='Толщина')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='brand',
            name='label',
            field=models.ImageField(blank=True, upload_to='brands/', verbose_name='Эмблема'),
        ),
        migrations.AddField(
            model_name='item',
            name='units',
            field=models.CharField(default=1, max_length=10, verbose_name='Единицы измерения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='tile_images/', verbose_name='Внешний вид'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='collection',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand'),
        ),
        migrations.AddField(
            model_name='item',
            name='characteristics',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.sizetype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.collection'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.kind'),
        ),
    ]
