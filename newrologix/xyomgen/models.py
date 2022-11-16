from django.db import models


class Product(models.Model):
    def __str__(self):
        return ""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='xyomgen/')
    price = models.FloatField()


class Category(models.Model):
    def __str__(self):
        return "{}|".format(self.category_name)

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, default="N/A")


class Brand(models.Model):
    def __str__(self):
        return "{}|".format(self.brand_name)

    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, default="N/A")


class UnitCount(models.Model):
    def __str__(self):
        return "{}|".format(self.count_name)

    unit_count_id = models.AutoField(primary_key=True)
    unit_count_name = models.CharField(max_length=255, default="N/A")


class Flavor(models.Model):
    def __str__(self):
        return "{}|".format(self.flavor_name)

    flavor_id = models.AutoField(primary_key=True)
    flavor_name = models.CharField(max_length=255, default="N/A")


class XyomgenProduct(models.Model):
    def __str__(self):
        return ""

    product_id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='xproduct_brand', on_delete=models.CASCADE)
    descriptionShort = models.CharField(max_length=255)
    productImage = models.CharField(max_length=255)
    quantity = models.IntegerField()
    count = models.CharField(max_length=255)
    unitCount = models.ForeignKey(UnitCount, related_name='xproduct_unitcount', on_delete=models.CASCADE)
    weight = models.FloatField()
    unitWeight = models.CharField(max_length=255)
    flavor = models.ForeignKey(Flavor, related_name='xproduct_flavor', on_delete=models.CASCADE)
    wholesalePrice = models.FloatField()
    retailPrice = models.FloatField()
    releaseDate = models.CharField(max_length=255)
    upc = models.CharField(max_length=255, default="N/A")
    sku = models.CharField(max_length=255, default="N/A")
    warnings = models.CharField(max_length=255, default="N/A")


class XProductCategoryMap(models.Model):
    def __str__(self):
        return ""

    map_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(XyomgenProduct, related_name='prodcatmap_product', on_delete=models.CASCADE)
"""
'productName', 'brand', 'descriptionShort',
           'productImage', 'categories', 'quantity', 'count',
           'countUnit', 'weight', 'weightUnit', 'defaultDosing', 'flavor',
           'wholesalePrice', 'retailPrice',
           'releaseDate', 'upc', 'sku', 'medPaxSku', 'medPaxDetails',
           'supplementalFactsHTML', 'descriptionFull', 'warnings'
"""