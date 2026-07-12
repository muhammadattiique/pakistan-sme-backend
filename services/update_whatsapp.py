from database import SessionLocal
from models import Business

from services.whatsapp_checker import check_whatsapp



def update_whatsapp_status():

    db = SessionLocal()


    businesses = (
        db.query(Business)
        .all()
    )


    updated = 0


    for business in businesses:


        if business.phone:

            business.has_whatsapp = (
                check_whatsapp(
                    business.phone
                )
            )

            updated += 1



    db.commit()

    db.close()


    return updated



if __name__ == "__main__":

    count = update_whatsapp_status()

    print(
        f"Updated {count} businesses"
    )