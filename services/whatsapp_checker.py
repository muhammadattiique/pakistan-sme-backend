import re


def normalize_phone(phone: str):

    if not phone:
        return None

    phone = re.sub(
        r"[^\d+]",
        "",
        phone
    )

    return phone



def check_whatsapp(phone: str):

    """
    Prototype WhatsApp checker.

    For public business numbers:
    - if phone exists → mark possible WhatsApp
    - real verification requires WhatsApp Business API
    """

    phone = normalize_phone(phone)

    if not phone:
        return False


    # Pakistan number validation

    pakistan_patterns = [

        r"^\+92\d{10}$",
        r"^92\d{10}$",
        r"^03\d{9}$"

    ]


    for pattern in pakistan_patterns:

        if re.match(pattern, phone):

            return True


    return False