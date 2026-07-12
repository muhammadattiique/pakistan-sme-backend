from database import SessionLocal
from models import Business

db = SessionLocal()

updated = 0

for business in db.query(Business).all():

    name = (business.name or "").lower()

    # Software House
    if any(word in name for word in [
        "software",
        "tech",
        "technology",
        "technologies",
        "digital",
        "developer",
        "solution",
        "systems"
    ]):
        business.industry = "Software House"

    # Pharmacy
    elif any(word in name for word in [
        "pharmacy",
        "medical store",
        "chemist"
    ]):
        business.industry = "Pharmacy"

    # Hospital
    elif any(word in name for word in [
        "hospital",
        "clinic"
    ]):
        business.industry = "Hospital"

    # Restaurant
    elif any(word in name for word in [
        "restaurant",
        "pizza",
        "burger",
        "bbq",
        "cafe",
        "coffee"
    ]):
        business.industry = "Restaurant"

    # Hotel
    elif any(word in name for word in [
        "hotel",
        "guest house"
    ]):
        business.industry = "Hotel"

    updated += 1

db.commit()

print(f"Updated {updated} businesses.")

db.close()