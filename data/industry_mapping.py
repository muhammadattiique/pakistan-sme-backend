"""
Maps OpenStreetMap tags to clean business industries.
"""

INDUSTRY_MAPPING = {

    # ==========================
    # FOOD
    # ==========================

    ("amenity", "restaurant"): "Restaurant",
    ("amenity", "cafe"): "Cafe",
    ("amenity", "fast_food"): "Fast Food",
    ("amenity", "food_court"): "Food Court",
    ("amenity", "ice_cream"): "Ice Cream",
    ("amenity", "bar"): "Restaurant",

    # ==========================
    # HEALTH
    # ==========================

    ("amenity", "hospital"): "Hospital",
    ("amenity", "clinic"): "Clinic",
    ("amenity", "doctors"): "Clinic",
    ("amenity", "dentist"): "Dental Clinic",
    ("shop", "pharmacy"): "Pharmacy",
    ("healthcare", "laboratory"): "Laboratory",

    # ==========================
    # EDUCATION
    # (Optional - keep if needed)
    # ==========================

    ("amenity", "school"): "School",
    ("amenity", "college"): "College",
    ("amenity", "university"): "University",

    # ==========================
    # SHOPS
    # ==========================

    ("shop", "supermarket"): "Supermarket",
    ("shop", "convenience"): "Grocery Store",
    ("shop", "bakery"): "Bakery",
    ("shop", "clothes"): "Clothing Store",
    ("shop", "shoes"): "Shoe Store",
    ("shop", "electronics"): "Electronics Store",
    ("shop", "computer"): "Computer Shop",
    ("shop", "mobile_phone"): "Mobile Shop",
    ("shop", "furniture"): "Furniture Store",
    ("shop", "hardware"): "Hardware Store",
    ("shop", "books"): "Book Store",
    ("shop", "stationery"): "Stationery Store",
    ("shop", "gift"): "Gift Shop",
    ("shop", "cosmetics"): "Cosmetics Store",
    ("shop", "jewelry"): "Jewelry Store",
    ("shop", "sports"): "Sports Store",
    ("shop", "car"): "Car Dealer",
    ("shop", "car_parts"): "Auto Parts",
    ("shop", "tyres"): "Tyre Shop",

    # ==========================
    # OFFICE
    # ==========================

    ("office", "it"): "Software House",
    ("office", "company"): "Company",
    ("office", "consulting"): "Consulting Firm",
    ("office", "lawyer"): "Law Firm",
    ("office", "accountant"): "Accounting Firm",
    ("office", "insurance"): "Insurance Company",
    ("office", "architect"): "Architecture Firm",
    ("office", "engineer"): "Engineering Firm",
    ("office", "estate_agent"): "Real Estate Agency",

    # ==========================
    # TOURISM
    # ==========================

    ("tourism", "hotel"): "Hotel",
    ("tourism", "guest_house"): "Guest House",
    ("tourism", "hostel"): "Hostel",

    # ==========================
    # SERVICES
    # ==========================

    ("shop", "beauty"): "Beauty Salon",
    ("shop", "hairdresser"): "Hair Salon",
    ("shop", "laundry"): "Laundry",
    ("shop", "tailor"): "Tailor",
    ("shop", "travel_agency"): "Travel Agency",

    # ==========================
    # INDUSTRY
    # ==========================

    ("industrial", "factory"): "Factory",
    ("industrial", "manufacturing"): "Manufacturer",

    # ==========================
    # FUEL
    # ==========================

    ("amenity", "fuel"): "Petrol Pump",
}