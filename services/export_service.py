import csv
from pathlib import Path

from sqlalchemy.orm import Session

from models import Business



EXPORT_FOLDER = Path("exports")


EXPORT_FOLDER.mkdir(
    exist_ok=True
)



def export_businesses(
    db: Session
):

    businesses = db.query(
        Business
    ).all()


    file_path = (
        EXPORT_FOLDER /
        "businesses.csv"
    )


    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:


        writer = csv.writer(file)


        writer.writerow([

            "id",
            "name",
            "industry",
            "city",
            "address",
            "website",
            "email",
            "phone",
            "whatsapp",
            "latitude",
            "longitude"

        ])



        for business in businesses:


            writer.writerow([

                business.id,

                business.name,

                business.industry,

                business.city,

                business.address,

                business.website,

                business.email,

                business.phone,

                business.whatsapp,

                business.latitude,

                business.longitude

            ])


    return str(file_path)