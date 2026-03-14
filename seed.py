import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modular_system.settings')
django.setup()

from vendor.models import VendorModel
from product.models import ProductModel
from course.models import CourseModel
from certification.models import CertificationModel
from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping

def run_seed():
    print("Seeding data...")

    # 1. Create Masters
    v1 = VendorModel.objects.get_or_create(name="Microsoft", code="MSFT01", description="Tech Giant")[0]
    p1 = ProductModel.objects.get_or_create(name="Azure Cloud", code="AZ01", description="Cloud Platform")[0]
    c1 = CourseModel.objects.get_or_create(name="Azure Fundamentals", code="AZ900", description="Beginner Course")[0]
    cert1 = CertificationModel.objects.get_or_create(name="Microsoft Certified: Fundamentals", code="MCF01")[0]

    # 2. Create Mappings (The "Manual" Logic)
    # Link Vendor to Product
    VendorProductMapping.objects.get_or_create(
        vendor=v1, 
        product=p1, 
        primary_mapping=True
    )

    # Link Product to Course
    ProductCourseMapping.objects.get_or_create(
        product=p1, 
        course=c1, 
        primary_mapping=True
    )

    # Link Course to Certification
    CourseCertificationMapping.objects.get_or_create(
        course=c1, 
        certification=cert1, 
        primary_mapping=True
    )

    print("Seeding completed successfully!")

if __name__ == "__main__":
    run_seed()