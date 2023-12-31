
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('GPU', 'Graphics Card'), ('CPU', 'Central Processor'), ('RAM', 'Memory')], max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 'really bad'), (2, 'bad'), (3, 'okay'), (4, 'good'), (5, 'great')], default=0, null=True),
        ),
    ]
