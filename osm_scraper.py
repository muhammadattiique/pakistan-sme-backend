import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

def get_businesses(city):

    query = f"""
    [out:json][timeout:25];

    area["name"="{city}"]->.searchArea;

    (
      node["shop"](area.searchArea);
      node["office"](area.searchArea);
      node["craft"](area.searchArea);
      node["amenity"="restaurant"](area.searchArea);
      node["amenity"="bank"](area.searchArea);
      node["amenity"="clinic"](area.searchArea);
    );

    out body;
    """

    response = requests.post(
        OVERPASS_URL,
        data=query,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("Status Code:", response.status_code)
    print("Response:")
    print(response.text[:500])  # Print first 500 characters

    if response.status_code == 200:
        return response.json()

    return None