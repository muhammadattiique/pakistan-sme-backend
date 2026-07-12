import re
import requests

from database import SessionLocal
from models import Business


# ==================================================
# PATTERNS
# ==================================================

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


PHONE_PATTERN = re.compile(
    r"(\+92|0092|0)?\s?\d{3}\s?\d{7}"
)


WHATSAPP_PATTERN = re.compile(
    r"https?://(?:wa\.me|api\.whatsapp\.com)/[^\s\"']+"
)



# ==================================================
# URL NORMALIZER
# ==================================================

def normalize_url(url):

    if not url:
        return None


    url = url.strip()


    if not url.startswith("http"):

        url = "https://" + url


    return url



# ==================================================
# EXTRACT CONTACTS
# ==================================================

def extract_contacts(html):

    emails = EMAIL_PATTERN.findall(html)

    phones = PHONE_PATTERN.findall(html)


    whatsapp_links = WHATSAPP_PATTERN.findall(
        html
    )


    return {

        "email":
            emails[0]
            if emails else None,


        "phone":
            phones[0]
            if phones else None,


        "whatsapp":
            whatsapp_links[0]
            if whatsapp_links else None

    }




# ==================================================
# WEBSITE SCANNER
# ==================================================

def scan_website(url):

    url = normalize_url(url)


    if not url:

        return {

            "email": None,
            "phone": None,
            "whatsapp": None

        }


    try:

        response = requests.get(

            url,

            timeout=10,

            headers={
                "User-Agent":
                "Mozilla/5.0"
            }

        )


        response.raise_for_status()


        return extract_contacts(
            response.text
        )


    except Exception:


        return {

            "email": None,

            "phone": None,

            "whatsapp": None

        }




# ==================================================
# DATABASE UPDATE
# ==================================================

def update_whatsapp():

    db = SessionLocal()


    businesses = (

        db.query(Business)

        .all()

    )


    updated = 0


    whatsapp_count = 0



    for business in businesses:


        result = None


        # Scan website if available

        if business.website:

            result = scan_website(
                business.website
            )


        has_whatsapp = False



        if business.whatsapp:

            has_whatsapp = True



        if result:


            if result["whatsapp"]:

                business.whatsapp = (
                    result["whatsapp"]
                )

                has_whatsapp = True



            if not business.email:

                business.email = (
                    result["email"]
                )


            if not business.phone:

                business.phone = (
                    result["phone"]
                )



        # Existing phone number also counts

        if business.phone:

            has_whatsapp = True



        business.has_whatsapp = has_whatsapp



        if has_whatsapp:

            whatsapp_count += 1



        updated += 1



    db.commit()

    db.close()



    print(
        "Businesses checked:",
        updated
    )


    print(
        "WhatsApp available:",
        whatsapp_count
    )





if __name__ == "__main__":

    update_whatsapp()