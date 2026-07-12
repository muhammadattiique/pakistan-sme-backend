from services.osm_collector import collect_businesses

businesses = collect_businesses("Lahore")

print(f"Found {len(businesses)} businesses")

for business in businesses[:5]:
    print(business)