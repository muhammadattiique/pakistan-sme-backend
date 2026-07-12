from database import SessionLocal
from crud import BusinessCRUD

db = SessionLocal()

crud = BusinessCRUD(db)

business = crud.create_business(
    {
        "name": "ABC Traders",
        "industry": "Trading",
        "website": "https://abctraders.pk",
        "email": "info@abctraders.pk",
        "phone": "03123456789",
        "address": "Lahore",
        "city": "Lahore",
        "has_whatsapp": False,
        "description": "Trading Company"
    }
)

print("Saved:", business.name)