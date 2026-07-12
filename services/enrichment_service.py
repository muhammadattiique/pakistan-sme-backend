from sqlalchemy.orm import Session

from models import Business

from services.website_enricher import scan_website



def run_enrichment(
    db: Session,
    batch_size: int = 50
):


    businesses = (

        db.query(Business)

        .filter(
            Business.website.isnot(None)
        )

        .filter(
            Business.email.is_(None)
        )

        .limit(batch_size)

        .all()

    )


    processed = 0



    for business in businesses:


        result = scan_website(

            business.website

        )


        if result:


            if result.get("email"):

                business.email = result["email"]



            if result.get("phone"):

                business.phone = result["phone"]



            if result.get("whatsapp"):

                business.whatsapp = result["whatsapp"]



        processed += 1



    db.commit()



    return {

        "processed":

        processed,


        "remaining":

        db.query(Business)

        .filter(
            Business.website.isnot(None)
        )

        .filter(
            Business.email.is_(None)
        )

        .count()

    }