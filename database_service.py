from sqlalchemy.orm import Session
from models import Business


class DatabaseService:

    def __init__(self, db: Session):
        self.db = db

    def business_exists(self, website):

        return (
            self.db.query(Business)
            .filter(Business.website == website)
            .first()
        )

    def add_business(self, data):

        business = Business(**data)

        self.db.add(business)

        self.db.commit()

        self.db.refresh(business)

        return business