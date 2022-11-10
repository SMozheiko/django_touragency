from django.db import models

# Create your models here.


class Brand(models.Model):
    """Tile brand"""
    title = models.CharField(
        verbose_name='Бренд', max_length=100, unique=True, null=False
    )
    label = models.ImageField(
        verbose_name='Эмблема', upload_to='brands/', blank=True
    )

    def __str__(self):
        return self.title


class Kind(models.Model):
    """Kind of tile"""
    title = models.CharField(
        verbose_name='разновидность',
        max_length=100,
        null=False
    )

    def __str__(self):
        return self.title


class SizeType(models.Model):
    """Physical characteristics"""
    length = models.FloatField(verbose_name='Длинна', null=False)
    width = models.FloatField(verbose_name='Ширина', null=False)
    thickness = models.FloatField(verbose_name='Толщина', null=False)

    def __str__(self):
        return '{} x {} x {} мм'.format(
            self.length, self.width, self.thickness
        )


class Collection(models.Model):
    """Table with kinds of catalog types: food, goods, fishing equipment"""
    title = models.CharField(
        verbose_name='Раздел', max_length=128, unique=True
    )
    description = models.TextField(
        verbose_name='Описание раздела', blank=True
    )
    label = models.ImageField(
        verbose_name='Обложка', upload_to='collections_labels/', blank=True
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=False
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    """Catalog item"""
    title = models.CharField(
        verbose_name='Название', max_length=256, null=False, unique=True
    )
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    characteristics = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    kind = models.ForeignKey(Kind, on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        verbose_name='Описание товара', blank=True
    )
    units = models.CharField(
        verbose_name='Единицы измерения', max_length=10
    )
    image = models.ImageField(
        verbose_name='Внешний вид', upload_to='tile_images/', blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2
    )
    count = models.IntegerField(
        verbose_name='Остаток на складе', default=0
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Slide(models.Model):
    """Slide images for collection slider"""
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name='Слайд', upload_to='tile_images/', blank=True
    )

    def __str__(self):
        return self.collection.title + '_slide_' + str(self.pk)
