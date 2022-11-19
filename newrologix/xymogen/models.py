from django.db import models


class Product(models.Model):
    def __str__(self):
        return ""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Xymogen/')
    price = models.FloatField()


class Category(models.Model):
    def __str__(self):
        return "{}|".format(self.category_name)

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, default="N/A")

    class Meta:
        unique_together = ('category_name',)


class Brand(models.Model):
    def __str__(self):
        return "{}|".format(self.brand_name)

    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, default="N/A")

    class Meta:
        unique_together = ('brand_name',)


class UnitCount(models.Model):
    def __str__(self):
        return "{}|".format(self.count_name)

    unit_count_id = models.AutoField(primary_key=True)
    unit_count_name = models.CharField(max_length=255, default="N/A")

    class Meta:
        unique_together = ('unit_count_name',)


class Flavor(models.Model):
    def __str__(self):
        return "{}|".format(self.flavor_name)

    flavor_id = models.AutoField(primary_key=True)
    flavor_name = models.CharField(max_length=255, default="N/A")

    class Meta:
        unique_together = ('flavor_name',)


class XymogenProduct(models.Model):
    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|".fomrat(self.productName,
                    self.brand, self.descriptionShort,
                    self.wholesalePrice, self.retailPrice,
                    self.releaseDate)

    product_id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='xproduct_brand', on_delete=models.CASCADE)
    descriptionShort = models.CharField(max_length=255)
    descriptionFull = models.CharField(max_length=1023)
    supplementFactsHTML = models.CharField(max_length=255, blank=True, null=True)
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
    drs = models.CharField(max_length=255, blank=True, null=True)
    upc = models.CharField(max_length=255, default="N/A")
    sku = models.CharField(max_length=255, default="N/A")
    warnings = models.CharField(max_length=255, default="N/A")


class XProductCategoryMap(models.Model):
    def __str__(self):
        return ""

    map_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(XymogenProduct, related_name='productmap_product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='productmap_category', on_delete=models.CASCADE)


class XProductDefaultDosingMap(models.Model):
    def __str__(self):
        return ""

    map_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(XymogenProduct, related_name='dosingmap_product', on_delete=models.CASCADE)
    #dose = models.ForeignKey(, related_name='dosingmap_product', on_delete=models.CASCADE)

"""
'productName', 'brand', 'descriptionShort',
           'productImage', 'categories', 'quantity', 'count',
           'countUnit', 'weight', 'weightUnit', 'defaultDosing', 'flavor',
           'wholesalePrice', 'retailPrice',
           'releaseDate', 'upc', 'sku', 'medPaxSku', 'medPaxDetails',
           'supplementalFactsHTML', 'descriptionFull', 'warnings'
"""