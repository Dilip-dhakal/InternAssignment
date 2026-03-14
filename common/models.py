from django.db import models
from abstract.models import  BaseModel
import uuid

class MasterCommonModels(BaseModel):
    id=models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False,primary_key=True)
    name=models.TextField(max_length=150)
    code=models.CharField(max_length=30,unique=True,blank=False)
    description=models.CharField(blank=True,max_length=200)
    
    class Meta:
        abstract=True