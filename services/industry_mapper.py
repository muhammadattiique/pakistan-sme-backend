from data.industry_mapping import INDUSTRY_MAPPING


SEARCH_ORDER = [
    "amenity",
    "shop",
    "office",
    "tourism",
    "industrial",
    "healthcare",
]


def get_industry(tags: dict) -> str | None:
    """
    Convert OpenStreetMap tags into a clean industry name.
    """

    for key in SEARCH_ORDER:

        value = tags.get(key)

        if not value:
            continue

        industry = INDUSTRY_MAPPING.get((key, value))

        if industry:
            return industry

    return None