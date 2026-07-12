from sqlalchemy.orm import Session

from services.osm_collector import collect_businesses
import crud


# ==========================================================
# COLLECT CITY BUSINESSES
# ==========================================================

def collect_city(
    city: str,
    db: Session,
):
    """
    Complete collection pipeline:

    City
      ↓
    OpenStreetMap
      ↓
    Normalize data
      ↓
    Insert into database
    """


    # Step 1: Collect from OSM

    businesses = collect_businesses(
        city
    )


    if not businesses:

        return {
            "city": city,
            "collected": 0,
            "inserted": 0,
            "message": "No businesses found",
        }


    # Step 2: Insert into database

    inserted = crud.bulk_create_businesses(
        db,
        businesses,
    )


    return {

        "city": city,

        "collected": len(
            businesses
        ),

        "inserted": inserted,

        "message":
        "Collection completed successfully",

    }