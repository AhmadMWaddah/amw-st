import pathlib

from django.db import models
from django.urls import reverse


def default_image():
    return 'default/default.png'


def upload_category_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'categories/{self.slug}{ext}'


def upload_toy_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'toys/{self.slug}{ext}'


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Slug', unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(verbose_name='Image', upload_to=upload_category_image, default=default_image,
                              blank=True, null=True)

    @property
    def get_toys(self):
        return Toy.objects.filter(category=self.name)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name', ]

    def get_absolute_url(self):
        return reverse('toys:details_category', kwargs={'slug': str(self.slug)})

    def __str__(self):
        return f'{self.name}'


class Toy(models.Model):
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=255)
    sku = models.IntegerField(verbose_name='SKU')
    slug = models.SlugField(verbose_name='Slug', unique=True)
    description = models.TextField(verbose_name='Description')
    barcode = models.IntegerField(verbose_name='Barcode')
    weight = models.DecimalField(verbose_name='Weight', max_digits=5, decimal_places=2)
    height = models.DecimalField(verbose_name='Height', max_digits=5, decimal_places=2)
    length = models.DecimalField(verbose_name='Length', max_digits=5, decimal_places=2)
    width = models.DecimalField(verbose_name='Width', max_digits=5, decimal_places=2)
    price = models.DecimalField(verbose_name='Price', max_digits=6, decimal_places=2)
    age = models.DecimalField(verbose_name='Age', max_digits=4, decimal_places=2)
    inventory = models.IntegerField(verbose_name='Inventory')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    image = models.ImageField(verbose_name='Image', upload_to=upload_toy_image, default=default_image,
                              blank=True, null=True)

    @property
    def dimensions(self):
        dimensions = f'{self.length} x {self.width} x {self.height}'
        return dimensions

    @property
    def in_stock(self):
        if self.inventory > 0:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('toys:details_toy', kwargs={'slug': str(self.slug)})

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f'{self.name}'
