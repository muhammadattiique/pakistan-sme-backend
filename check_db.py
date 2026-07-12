from database import SessionLocal
from models import Business


db = SessionLocal()


count = db.query(Business).count()

print("Total businesses:", count)


records = (
    db.query(Business)
    .limit(5)
    .all()
)


for b in records:

    print(
        b.id,
        b.name,
        b.industry,
        b.city,
        b.phone
    )


db.close()