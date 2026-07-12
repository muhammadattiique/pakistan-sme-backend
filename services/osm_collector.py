from typing import Any
import requests
import time

from services.industry_mapping import INDUSTRY_MAPPING
from services.business_filters import is_business_name


# ==========================================================
# OVERPASS SERVERS
# ==========================================================

OVERPASS_SERVERS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]


# ==========================================================
# MAJOR PAKISTAN CITIES
# ==========================================================

CITY_BOXES = {

    "Lahore": (31.35, 74.10, 31.70, 74.45),
    "Karachi": (24.75, 66.85, 25.25, 67.45),
    "Islamabad": (33.55, 72.90, 33.85, 73.30),
    "Rawalpindi": (33.45, 72.95, 33.75, 73.20),
    "Faisalabad": (31.30, 72.95, 31.60, 73.25),
    "Multan": (30.05, 71.35, 30.35, 71.60),
    "Peshawar": (33.90, 71.40, 34.10, 71.70),
    "Quetta": (30.10, 66.85, 30.35, 67.20),
    "Sialkot": (32.45, 74.45, 32.65, 74.65),
    "Gujranwala": (32.05, 74.05, 32.30, 74.30),
}


# ==========================================================
# BUSINESS TAGS
# ==========================================================

BUSINESS_TAGS = [

    "restaurant",
    "fast_food",
    "cafe",
    "bakery",
    "pharmacy",
    "hospital",
    "clinic",
    "dentist",
    "doctors",

    "school",
    "college",
    "university",

    "bank",
    "atm",

    "hotel",
    "guest_house",

    "supermarket",
    "convenience",
    "clothes",
    "shoes",
    "electronics",
    "mobile_phone",
    "computer",
    "hardware",
    "books",
    "furniture",

    "car_repair",
    "car_wash",
    "fuel",

    "beauty",
    "hairdresser",
    "gym",

]


# ==========================================================
# BUILD QUERY
# ==========================================================

def build_query(city: str):

    if city not in CITY_BOXES:
        raise ValueError(f"Unsupported city: {city}")

    south, west, north, east = CITY_BOXES[city]

    query = """
[out:json][timeout:180];
(
"""

    for tag in BUSINESS_TAGS:

        query += f"""
node["amenity"="{tag}"]({south},{west},{north},{east});
way["amenity"="{tag}"]({south},{west},{north},{east});

node["shop"="{tag}"]({south},{west},{north},{east});
way["shop"="{tag}"]({south},{west},{north},{east});

node["office"="{tag}"]({south},{west},{north},{east});
way["office"="{tag}"]({south},{west},{north},{east});
"""

    query += """
);
out center tags;
"""

    return query


# ==========================================================
# DOWNLOAD FROM OVERPASS
# ==========================================================

def fetch_overpass_data(query: str):

    last_error = None

    for server in OVERPASS_SERVERS:

        try:

            print("Trying:", server)

            response = requests.post(
                server,
                data={"data": query},
                headers={
                    "User-Agent": "Pakistan-SME-Collector/4.0"
                },
                timeout=180,
            )

            response.raise_for_status()

            data = response.json()

            print(
                "Downloaded:",
                len(data.get("elements", []))
            )

            return data

        except Exception as e:

            print(e)

            last_error = e

            time.sleep(3)

    raise Exception(last_error)
    # ==========================================================
# SMART INDUSTRY CLASSIFIER
# ==========================================================

def classify_industry(name: str, tags: dict):

    text = (
        (name or "") + " " +
        " ".join(str(v) for v in tags.values())
    ).lower()

    # -------------------------
    # Software / IT
    # -------------------------
    if any(word in text for word in [
        "software",
        "software house",
        "technology",
        "technologies",
        "tech",
        "digital",
        "developer",
        "developers",
        "systems",
        "solution",
        "solutions",
        "web",
        "app",
        "it company",
        "programming",
        "coding",
    ]):
        return "Software House"

    # -------------------------
    # Pharmacy
    # -------------------------
    if any(word in text for word in [
        "pharmacy",
        "medical store",
        "chemist",
        "drug",
    ]):
        return "Pharmacy"

    # -------------------------
    # Hospital
    # -------------------------
    if any(word in text for word in [
        "hospital",
        "clinic",
        "health center",
        "medical centre",
    ]):
        return "Hospital"

    # -------------------------
    # Restaurant
    # -------------------------
    if any(word in text for word in [
        "restaurant",
        "pizza",
        "burger",
        "bbq",
        "biryani",
        "food",
        "cafe",
        "coffee",
    ]):
        return "Restaurant"

    # -------------------------
    # Hotel
    # -------------------------
    if any(word in text for word in [
        "hotel",
        "guest house",
        "guesthouse",
        "motel",
    ]):
        return "Hotel"

    # -------------------------
    # Education
    # -------------------------
    if "school" in text:
        return "School"

    if "college" in text:
        return "College"

    if "university" in text:
        return "University"

    # -------------------------
    # Finance
    # -------------------------
    if "bank" in text:
        return "Bank"

    # -------------------------
    # Textile
    # -------------------------
    if any(word in text for word in [
        "textile",
        "garment",
        "garments",
        "fashion",
        "clothing",
    ]):
        return "Textile"

    # -------------------------
    # Factory
    # -------------------------
    if any(word in text for word in [
        "factory",
        "manufacturing",
        "industry",
    ]):
        return "Factory"

    # -------------------------
    # Supermarket
    # -------------------------
    if any(word in text for word in [
        "mart",
        "supermarket",
        "cash & carry",
        "cash and carry",
    ]):
        return "Supermarket"

    # -------------------------
    # Bakery
    # -------------------------
    if "bakery" in text:
        return "Bakery"

    # -------------------------
    # Petrol Pump
    # -------------------------
    if any(word in text for word in [
        "petrol",
        "fuel",
        "shell",
        "caltex",
        "pso",
        "total",
    ]):
        return "Petrol Pump"

    # =====================================================
    # Fallback to OSM mapping
    # =====================================================

    for key in ("amenity", "shop", "office"):

        value = tags.get(key)

        if value in INDUSTRY_MAPPING:
            return INDUSTRY_MAPPING[value]

    return "Other"


# ==========================================================
# NORMALIZE BUSINESS
# ==========================================================

def normalize_business(element: dict[str, Any], city: str):

    tags = element.get("tags", {})

    name = tags.get("name")

    if not name:
        return None

    if not is_business_name(name):
        return None

    lat = element.get("lat")
    lon = element.get("lon")

    if lat is None:

        center = element.get("center", {})

        lat = center.get("lat")
        lon = center.get("lon")

    industry = classify_industry(
        name,
        tags,
    )

    return {

        "osm_id": str(element["id"]),

        "name": name,

        "industry": industry,

        "city": city,

        "address": tags.get("addr:street", ""),

        "website": tags.get("website"),

        "email": tags.get("email"),

        "phone": tags.get("phone"),

        "whatsapp": None,

        "latitude": lat,

        "longitude": lon,

        "source": "OpenStreetMap",

    }


# ==========================================================
# COLLECT BUSINESSES
# ==========================================================

def collect_businesses(city: str):

    query = build_query(city)

    data = fetch_overpass_data(query)

    businesses = []

    seen = set()

    for element in data.get("elements", []):

        business = normalize_business(
            element,
            city,
        )

        if business is None:
            continue

        if business["osm_id"] in seen:
            continue

        seen.add(
            business["osm_id"]
        )

        businesses.append(
            business
        )

    print(
        "Businesses collected:",
        len(businesses)
    )

    return businesses