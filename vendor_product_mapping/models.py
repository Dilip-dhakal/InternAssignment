from django.db import models
from abstract.models import BaseModel
from vendor.models import VendorModel
from product.models import ProductModel

# Create your models here.

class VendorProductMapping(BaseModel):
    vendor=models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    primary_mapping=models.BooleanField(default=False)
