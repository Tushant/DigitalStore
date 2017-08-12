import random
import string
import os

from django.contrib.auth.models import User
from django.db import models


def token_generator():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(9))

DAY = (( 'Sun', 'Sunday'),
	   ( 'Mon', 'Monday'),
	   ( 'Tue', 'Tuesday'),
	   ( 'Wed', 'Wednesday'),
	   ( 'Thu', 'Thursday'),
	   ( 'Fri', 'Friday'),
	   ( 'Sat', 'Saturday')
	)

class OpeningHours(models.Model):
    store = models.ForeignKey('Store', related_name="opening_hour")
    weekday = models.CharField(choices=DAY, max_length=12)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    class Meta:
    	verbose_name = 'Opening Hour'
    	verbose_name_plural = 'Opening Hours'

    def ___str__(self):
        return '{} {} - {}'.format(self.weekday, str(self.opening_hour), str(self.closing_hour))

class Store(models.Model):
    merchant = models.ForeignKey(User, blank=True, null=False)
    token = models.CharField(default=token_generator, max_length=20, unique=True, editable=False)
    name_of_legal_entity = models.CharField(max_length=250, blank=False, null=False)
    pan_number = models.CharField(max_length=20, blank=False, null=False)
    registered_office_address = models.CharField(max_length=200)
    name_of_store = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False)
    store_contact_number = models.PositiveIntegerField(blank=False, null=False)
    # store_long = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    # store_lat = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name = 'Store'

    def __str__(self):
    	return self.name_of_store

    class Meta:
    	verbose_name = 'Store'
    	verbose_name_plural = 'Stores'

class Product(models.Model):
    store = models.ForeignKey(Store)
    token = models.CharField(default=token_generator, max_length=20, unique=True, editable=False)
    image = models.ImageField(upload_to='products/images/')
    name_of_product = models.CharField(max_length=120, blank=False,null=False)
    description	= models.TextField(blank=False,null=False)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    is_active = models.BooleanField(default=True)
    # categories = models.ManyToManyField('Category',blank=True)


    def __str__(self):
    	return self.name_of_product

    class Meta:
    	verbose_name = 'Product'
    	verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name="product_image")
    image = models.ImageField(upload_to='products/images/')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def imageName(self):
    	return str(os.path.basename(self.image.name))

    def __str__(self):
    	return str(self.image)

    class Meta:
    	verbose_name = 'Product Image'
    	verbose_name_plural = 'Product Images'



# class VariationManager(models.Manager):
# 	def all(self):
# 		return super(VariationManager, self).filter(active=True)

# 	def sizes(self):
# 		return self.all().filter(category='size')

# 	def colors(self):
# 		return self.all().filter(category='color')



# VAR_CATEGORIES = (
# 		('size','size'),
# 		('color','color'),
# 	)


class StoreCategory(models.Model):
    STORE_CATEGORIES= (
        ('GROCERY', ('Grocery')),
        ('MEATS', ('Meats')),
        ('FOODS & BEVERAGES', ('Foods')),
        ('COMPUTERS', ('Computers')),
        ('ELECTRONICS', ('Electronics')),
        ('HOME & OUTDOOR', ('Home & Outdoor')),
        ('FASHION & BEAUTY', ('Fashion & Beauty')),
        ('HEALTH', ('Health')),
        ('SPORTS & FITNESS', ('Sports & Fitness')),
        ('BABY', ('Baby')),
        ('BOOKS', ('Books')),
    )

    product = models.ForeignKey(Product,null=True, on_delete=models.CASCADE)
    store_category = models.CharField(choices=STORE_CATEGORIES, default='GROCERY', max_length=30)
    # objects = VariationManager()

    class Meta:
    	verbose_name = 'Store Category'
    	verbose_name_plural = 'Store Categories'

    def __str__(self):
    	# return str(self.product.name_of_product)
    	return '{0} of category {1}' .format(self.product.name_of_product, str(self.store_category))
