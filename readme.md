Modular Entity and Mapping System
A Django REST Framework backend built with a modular architecture where every master entity and mapping relationship is isolated into its own Django application.

🚀 Objective
The goal of this project is to manage Master Entities (Vendor, Product, Course, Certification) and their inter-dependencies using a strict APIView-only approach, ensuring deep understanding of DRF basics and manual request handling.

🛠 Tech Stack
Framework: Django 6.0.3

API Engine: Django REST Framework (DRF)

Documentation: drf-yasg (Swagger/ReDoc)

Database: SQLite (Development)

📁 Project Structure
The project follows a modular "App-per-Entity" structure:

Master Apps: vendor, product, course, certification

Mapping Apps: vendor_product_mapping, product_course_mapping, course_certification_mapping

Core Apps: abstract (Base styles), common (Shared Master fields)

⚙️ Setup Instructions
Clone the Repository:

Bash
git clone <your-repo-link>
cd modular_system
Create Virtual Environment:

Bash
python -m venv env
source env/Scripts/activate  # Windows
Install Dependencies:

Bash
pip install django djangorestframework drf-yasg
Run Migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Seed Data:
Run the provided seed script to populate the database with sample entities and mappings:

Bash
python seed_data.py
Run Server:

Bash
python manage.py runserver
📖 API Documentation
Once the server is running, you can access the interactive documentation at:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

🛡 Validations Implemented
As per the assignment requirements, the following logic is strictly enforced:

Unique Code: Master entities cannot share the same identification code.

No Duplicate Mappings: Prevents linking the same parent-child pair twice.

Single Primary Mapping: Only one child can be marked as "Primary" for any given parent entity.

Soft Delete: Using is_active=False instead of hard database deletions.

🔍 API Usage Examples
Filter Products by Vendor
URL: GET /api/product/?vendor_id=<uuid>

Description: Returns all products mapped to a specific vendor.

Create a Mapping
URL: POST /api/vendor-product-mapping/

Body:

JSON
{
    "vendor": "uuid-here",
    "product": "uuid-here",
    "primary_mapping": true
}