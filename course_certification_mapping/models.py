from django.db import models
from abstract.models import BaseModel
from course.models import CourseModel
from certification.models import CertificationModel
# Create your models here.

class CourseCertificationMapping(BaseModel):
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    certification=models.ForeignKey(CertificationModel,on_delete=models.CASCADE)
    primary_mapping=models.BooleanField(default=False)