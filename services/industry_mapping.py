"""
Industry normalization for OpenStreetMap tags.
Only recognized business categories will be imported.
"""

INDUSTRY_MAPPING = {

    # ==========================
    # FOOD
    # ==========================

    "restaurant": "Restaurant",
    "fast_food": "Fast Food",
    "cafe": "Cafe",
    "bakery": "Bakery",
    "ice_cream": "Ice Cream",
    "food_court": "Food Court",

    # ==========================
    # HEALTH
    # ==========================

    "hospital": "Hospital",
    "clinic": "Clinic",
    "doctors": "Clinic",
    "dentist": "Dentist",
    "pharmacy": "Pharmacy",
    "laboratory": "Laboratory",

    # ==========================
    # EDUCATION
    # ==========================

    "school": "School",
    "college": "College",
    "university": "University",
    "kindergarten": "School",

    # ==========================
    # SHOPPING
    # ==========================

    "supermarket": "Supermarket",
    "convenience": "Grocery Store",
    "mall": "Shopping Mall",
    "clothes": "Clothing Store",
    "shoes": "Shoe Store",
    "electronics": "Electronics Store",
    "mobile_phone": "Mobile Shop",
    "computer": "Computer Shop",
    "hardware": "Hardware Store",
    "books": "Book Store",
    "furniture": "Furniture Store",
    "jewelry": "Jewellery Shop",
    "cosmetics": "Cosmetics Store",

    # ==========================
    # FINANCE
    # ==========================

    "bank": "Bank",
    "atm": "ATM",

    # ==========================
    # HOTELS
    # ==========================

    "hotel": "Hotel",
    "guest_house": "Guest House",
    "hostel": "Hostel",

    # ==========================
    # AUTOMOTIVE
    # ==========================

    "car_repair": "Auto Workshop",
    "car_wash": "Car Wash",
    "fuel": "Petrol Pump",

    # ==========================
    # BEAUTY
    # ==========================

    "beauty": "Beauty Salon",
    "hairdresser": "Barber Shop",

    # ==========================
    # FITNESS
    # ==========================

    "gym": "Gym",

    # ==========================
    # OFFICES
    # ==========================

    "company": "Company",
    "travel_agency": "Travel Agency",
    "estate_agent": "Real Estate",
    "lawyer": "Law Firm",
    "accountant": "Accounting Firm",

    # ==========================
    # INDUSTRY
    # ==========================

    "manufacturer": "Manufacturer",
    "factory": "Factory",
    "warehouse": "Warehouse",

    # ==========================
    # IT
    # ==========================

    "software": "Software House",
    "it": "IT Company",
}