# Generated by Django 4.2.3 on 2023-08-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_thumbnail'),
        ('order', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-id',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='user',
        ),
        migrations.AlterField(
            model_name='productorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.product'),
        ),
    ]
