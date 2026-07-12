from typing import Optional


# ==========================================================
# INDUSTRY MAPPING
# ==========================================================

INDUSTRY_MAP = {

    # Food
    "restaurant": "Restaurant",
    "fast_food": "Restaurant",
    "cafe": "Cafe",
    "bakery": "Bakery",
    "bar": "Food & Beverage",


    # Retail
    "supermarket": "Retail",
    "convenience": "Retail",
    "clothes": "Fashion Retail",
    "shoes": "Fashion Retail",
    "electronics": "Electronics",
    "mobile_phone": "Mobile Shop",
    "computer": "Computer & IT",
    "hardware": "Hardware Store",


    # Services
    "hairdresser": "Beauty & Salon",
    "beauty": "Beauty & Salon",
    "laundry": "Laundry Service",
    "car_repair": "Auto Service",
    "car_parts": "Auto Parts",


    # Professional
    "lawyer": "Legal Services",
    "accountant": "Accounting",
    "insurance": "Insurance",
    "real_estate_agent": "Real Estate",


    # Industry
    "factory": "Manufacturing",
    "workshop": "Workshop",
    "craft": "Skilled Trade",


    # Health
    "clinic": "Healthcare",
    "dentist": "Healthcare",
    "pharmacy": "Pharmacy",

}



# ==========================================================
# EXCLUDED TYPES
# ==========================================================

NON_BUSINESS_TYPES = {

    "park",
    "school",
    "college",
    "university",
    "mosque",
    "place_of_worship",
    "hospital",
    "graveyard",
    "playground",
    "bus_stop",
    "parking",
    "bench",
}



# ==========================================================
# CLASSIFY INDUSTRY
# ==========================================================

def classify_industry(
    raw_industry: Optional[str],
):

    if not raw_industry:

        return "Other"



    value = raw_industry.lower()



    if value in NON_BUSINESS_TYPES:

        return None



    if value in INDUSTRY_MAP:

        return INDUSTRY_MAP[value]



    return "Other"



# ==========================================================
# CHECK BUSINESS
# ==========================================================

def is_business(
    raw_industry: Optional[str],
):

    category = classify_industry(
        raw_industry
    )


    if category is None:

        return False


    return True