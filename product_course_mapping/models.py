from django.db import models
from abstract.models import BaseModel
from product.models import ProductModel
from course.models import CourseModel
# Create your models here.

class ProductCourseMapping(BaseModel):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    primary_mapping=models.BooleanField(default=False)