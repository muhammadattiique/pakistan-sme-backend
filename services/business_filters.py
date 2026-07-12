"""
Remove non-business objects from OSM.
"""

BAD_WORDS = {

    "junction",
    "interchange",
    "bridge",
    "road",
    "street",
    "park",
    "playground",
    "lake",
    "river",
    "canal",
    "graveyard",
    "cemetery",
    "mosque",
    "church",
    "temple",
    "railway",
    "station",
    "airport",
    "bus stop",
    "metro",
    "chowk",
    "square",
    "gate",
    "village",
    "town",
    "colony",
    "phase",
    "block",
}


def is_business_name(name: str) -> bool:

    if not name:
        return False

    lower = name.lower()

    for word in BAD_WORDS:
        if word in lower:
            return False

    return True