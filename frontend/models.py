from django.db import models
from django.contrib.auth import get_user_model
from users.models import *

# Create your models here.

class Blog(models.Model):
    blog_img = models.ImageField(blank=True, verbose_name='Blog Image', null=True, upload_to='uploads/')
    blog_title = models.CharField(max_length=100, verbose_name='Blog Title')
    blog_description = models.TextField(verbose_name='Description')
    blog_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.blog_title

    def img_url(self):
        if self.blog_img:
            return self.blog_img.url
        

class Restaurant(models.Model):
    img = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/')
    title = models.CharField(max_length=100, verbose_name='Package Name')
    # brand = models.CharField(max_length=100, verbose_name='Package Name')
    price = models.CharField(max_length=20, verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    delivery = models.CharField(max_length=20, verbose_name='Delivery Fee')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Restaurant'

    def __str__(self):
        return self.title

    def img_url(self):
        if self.img:
            return self.img.url
        

class Fashion(models.Model):
    img1 = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/' )
    img2 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    img3 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    img4 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/')
    product_detail = models.TextField(max_length=100, verbose_name='Package Details')
    vendor_brand = models.CharField(max_length=100, verbose_name='Brand')
    price = models.CharField(max_length=20, verbose_name='Price')
    size = models.CharField(max_length=20, verbose_name='Size')
    available_product = models.CharField(max_length=20, verbose_name='Available product')
    delivery_fee = models.CharField(max_length=20, verbose_name='Delivery Fee')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Fashion'

    def __str__(self):
        return self.product_detail

    def img1_url(self):
        if self.img1:
            return self.img1.url
        
    def img2_url(self):
        if self.img2:
            return self.img2.url

    def img3_url(self):
        if self.img3:
            return self.img3.url

    def img4_url(self):
        if self.img4:
            return self.img4.url
        
class Pastries(models.Model):
    image = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/' )
    detail = models.TextField(max_length=100, verbose_name='Package Details')
    vendor_brand = models.CharField(max_length=100, verbose_name='Brand')
    price = models.CharField(max_length=20, verbose_name='Price')
    delivery_fee = models.CharField(max_length=20, verbose_name='Delivery Fee')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Pastries'

    def __str__(self):
        return self.detail

    def image_url(self):
        if self.image:
            return self.image.url

class Gadgets(models.Model):
    img1 = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/' )
    img2 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    detail = models.TextField(max_length=500, verbose_name='Gadget Details')
    vendor_brand = models.CharField(max_length=100, verbose_name='Brand')
    price = models.CharField(max_length=20, verbose_name='Price')
    colour = models.CharField(max_length=20, verbose_name='Colour')
    available_product = models.CharField(max_length=20, verbose_name='No. of available Gadgets')
    delivery_fee = models.CharField(max_length=20, verbose_name='Delivery Fee')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Gadgets'

    def __str__(self):
        return self.detail

    def img1_url(self):
        if self.img1:
            return self.img1.url
        
    def img2_url(self):
        if self.img2:
            return self.img2.url

    
        
class SubscribeModel(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    email= models.EmailField()
    first_name = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    
    def __srf__(self):
        return self.first_name

# class Product(models.Model):
#     WEARS = "W"
#     PASTRIES = "P"
#     GADGETS = "G"
#     HOSTELS = "H"
#     RESTAURANTS = "R"
#     CHOOSE = ""

#     PRODUCT_TYPE = [
#         (WEARS, 'Wears'),
#         (PASTRIES, 'Pastries'),
#         (GADGETS, 'Gadgets'),
#         (HOSTELS, 'Hostels'),
#         (RESTAURANTS, 'Restaurants'),
#         (CHOOSE, 'Please Choose')

    # ]


    # BUNGALOW = "Bungalow"
    # DUPLEX = "Duplex"
    # FLAT = "Flat"
    # GLASSHOUSE = "Glasshouse"
    # STORY_BUILDING = "Story Building"
    # CHOOSE = ""

    # PROPERTY_TYPE = [

    #     (BUNGALOW, 'Bungalow'),
    #     (DUPLEX, 'Duplex'),
    #     (FLAT, 'Flat'),
    #     (GLASSHOUSE, 'Glass House'),
    #     (STORY_BUILDING, 'Story Building'),
    #     (CHOOSE, 'Please Choose')

    # ]


    # ONE = "100,000"
    # TWO = "150,00"
    # THREE = "200,000"
    # FOUR = "250,000"
    # FIVE = "300,000"
    # SIX = "350,000"
    # SEVEN = "400,000"
    # EIGHT = "450,000"
    # NINE = "500,000"
    # TEN = "550,000"
    # ONE1 = "600,000"
    # TWO2 = "650,000"
    # THREE3 = "700,000"
    # FOUR4 = "750,000"
    # FIVE5 = "800,000"
    # SIX6 = "850,000"
    # SEVEN7 = "900,000"
    # EIGHT8 = "950,000"
    # NINE9 = "1 Million"
    # TEN10 = "1.5 Million"
    # ONE11 = "2 Million"
    # TWO22 = "2.5 Million"
    # THREE33 = "3 Million"
    # FOUR44 = "3.5 Million"
    # FIVE55 = "4 Million"
    # SIX66 = "4.5 Million"
    # SEVEN77= "5 Million"
    # CHOOSE = ""

    # PRICE= [
    #      (ONE, ' 100,000'),
    #      (TWO, ' 150,000'),
    #      (THREE, ' 200,000'),
    #      (FOUR, ' 250,000'),
    #      (FIVE, ' 300,000'),
    #      (SIX, ' 350,000'),
    #      (SEVEN, ' 400,000'),
    #      (EIGHT, ' 450,000'),
    #      (NINE, ' 500,000'),
    #      (TEN, ' 550,000'),
    #      (ONE1, ' 600,000'),
    #      (TWO2, ' 650,000'),
    #      (THREE3, ' 700,000'),
    #      (FOUR4, ' 750,000'),
    #      (FIVE5, ' 800,000'),
    #      (SIX6, ' 850,000'),
    #      (SEVEN7, ' 900,000'),
    #      (EIGHT8, ' 950,000'),
    #      (NINE9, ' 1 Million'),
    #      (TEN10, ' 1.5 Million'),
    #      (ONE11, ' 2 Million'),
    #      (TWO22, ' 2.5 Million'),
    #      (THREE33, ' 3 Million'),
    #      (FOUR44, ' 3.5 Million'),
    #      (FIVE55, ' 4 Million'),
    #      (SIX66, ' 4.5 Million'),
    #      (SEVEN77, ' 5 Million'),
    #      (CHOOSE, 'Please Choose')
    # ]
    # product_img = models.ImageField(blank=True, verbose_name='Property image', null=True, upload_to='uploads/' )
    # img1 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    # img2 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    # img3 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    # product_title = models.CharField(max_length=100, verbose_name='Property Name')
    # # product_price = models.CharField(max_length=40, choices=PRICE, default=CHOOSE)
    # # listing_type = models.CharField(max_length=40, choices=PROPERTY_TYPE, default=CHOOSE)
    # product_desription = models.TextField(verbose_name='Description')
    # product_contact = models.CharField(max_length=20, verbose_name='Contact')
    # product_date = models.DateTimeField(auto_now_add=True)
    # # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product_type = models.CharField(max_length=40, choices=PRODUCT_TYPE, default=CHOOSE)
    # sponsored =models.BooleanField()
    # featured = models.BooleanField()


    # class Meta():
    #     verbose_name_plural = 'Product'

    # def __str__(self):
    #     return self.product_title

    # def img_url(self):
    #     if self.product_img:
    #         return self.product_img.url

    # def img1_url(self):
    #     if self.img1:
    #         return self.img1.url

    # def img2_url(self):
    #     if self.img2:
    #         return self.img2.url

    # def img3_url(self):
    #     if self.img3:
    #         return self.img3.url