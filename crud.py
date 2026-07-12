from typing import Any

from sqlalchemy import func
from sqlalchemy.orm import Session

import models
import schemas


# ==========================================================
# CREATE SINGLE BUSINESS
# ==========================================================

def create_business(
    db: Session,
    business: schemas.BusinessCreate,
):
    db_business = models.Business(
        **business.model_dump()
    )

    try:
        db.add(db_business)
        db.commit()
        db.refresh(db_business)
        return db_business

    except Exception:
        db.rollback()
        raise


# ==========================================================
# READ
# ==========================================================

def get_business(
    db: Session,
    business_id: int,
):
    return (
        db.query(models.Business)
        .filter(models.Business.id == business_id)
        .first()
    )


def get_business_by_osm_id(
    db: Session,
    osm_id: str,
):
    return (
        db.query(models.Business)
        .filter(models.Business.osm_id == osm_id)
        .first()
    )


# ==========================================================
# PAGINATED BUSINESSES
# ==========================================================

def get_businesses(
    db: Session,
    page: int = 1,
    limit: int = 20,
):

    if page < 1:
        page = 1

    if limit < 1:
        limit = 20

    offset = (page - 1) * limit

    total = (
        db.query(func.count(models.Business.id))
        .scalar()
    )

    businesses = (
        db.query(models.Business)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": (total + limit - 1) // limit,
        "items": businesses,
    }


# ==========================================================
# SEARCH
# ==========================================================

def search_businesses(
    db: Session,
    keyword: str | None = None,
    city: str | None = None,
    industry: str | None = None,
):

    query = db.query(models.Business)

    if keyword:
        query = query.filter(
            models.Business.name.ilike(f"%{keyword}%")
        )

    if city:
        query = query.filter(
            func.lower(models.Business.city)
            == city.lower()
        )

    if industry:
        query = query.filter(
            func.lower(models.Business.industry)
            == industry.lower()
        )

    return query.all()


# ==========================================================
# GET UNIQUE CITIES
# ==========================================================

def get_cities(db: Session):

    cities = (
        db.query(models.Business.city)
        .filter(models.Business.city.isnot(None))
        .distinct()
        .order_by(models.Business.city)
        .all()
    )

    return [city[0] for city in cities if city[0]]


# ==========================================================
# GET UNIQUE INDUSTRIES
# ==========================================================

def get_industries(db: Session):

    industries = (
        db.query(models.Business.industry)
        .filter(models.Business.industry.isnot(None))
        .distinct()
        .order_by(models.Business.industry)
        .all()
    )

    return [industry[0] for industry in industries if industry[0]]


# ==========================================================
# UPDATE
# ==========================================================

def update_business(
    db: Session,
    business_id: int,
    business: schemas.BusinessUpdate,
):

    db_business = get_business(
        db,
        business_id,
    )

    if not db_business:
        return None

    update_data = business.model_dump(
        exclude_unset=True
    )

    try:

        for field, value in update_data.items():
            setattr(
                db_business,
                field,
                value,
            )

        db.commit()
        db.refresh(db_business)

        return db_business

    except Exception:
        db.rollback()
        raise


# ==========================================================
# DELETE
# ==========================================================

def delete_business(
    db: Session,
    business_id: int,
):

    db_business = get_business(
        db,
        business_id,
    )

    if not db_business:
        return None

    try:

        db.delete(db_business)
        db.commit()

        return db_business

    except Exception:
        db.rollback()
        raise


# ==========================================================
# FAST BULK INSERT
# ==========================================================

def bulk_create_businesses(
    db: Session,
    businesses: list[dict[str, Any]],
):

    if not businesses:
        return 0

    incoming_ids = {
        item["osm_id"]
        for item in businesses
        if item.get("osm_id")
    }

    existing_ids = {
        row[0]
        for row in (
            db.query(models.Business.osm_id)
            .filter(
                models.Business.osm_id.in_(incoming_ids)
            )
            .all()
        )
    }

    new_businesses = []

    for item in businesses:

        osm_id = item.get("osm_id")

        if not osm_id:
            continue

        if osm_id in existing_ids:
            continue

        new_businesses.append(
            models.Business(**item)
        )

    if not new_businesses:
        return 0

    try:

        db.bulk_save_objects(
            new_businesses
        )

        db.commit()

        return len(new_businesses)

    except Exception:

        db.rollback()
        raise


# ==========================================================
# STATISTICS
# ==========================================================

def count_businesses(
    db: Session,
):
    return db.query(models.Business).count()


def count_by_city(
    db: Session,
    city: str,
):
    return (
        db.query(models.Business)
        .filter(models.Business.city == city)
        .count()
    )


def count_by_industry(
    db: Session,
    industry: str,
):
    return (
        db.query(models.Business)
        .filter(models.Business.industry == industry)
        .count()
    )