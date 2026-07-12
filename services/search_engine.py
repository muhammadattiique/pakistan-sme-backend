from sqlalchemy.orm import Session
from sqlalchemy import or_

from models import Business



def search_businesses(
    db: Session,
    keyword: str | None = None,
    city: str | None = None,
    industry: str | None = None,
):

    query = db.query(Business)


    if keyword:

        keyword = keyword.lower()

        query = query.filter(

            or_(

                Business.name.ilike(
                    f"%{keyword}%"
                ),

                Business.industry.ilike(
                    f"%{keyword}%"
                ),

                Business.address.ilike(
                    f"%{keyword}%"
                )

            )

        )


    if city:

        query = query.filter(

            Business.city.ilike(
                city
            )

        )


    if industry:

        query = query.filter(

            Business.industry.ilike(
                industry
            )

        )


    return query.all()