# nesting dict in a list
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lilly", "Dijon"],
#         "total_visits": 10
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Muchen", "Hamburg"],
#         "total_visits": 5
#     }
# }

# nesting dict in list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lilly", "Dijon"],
        "total_visits": 10
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Muchen", "Hamburg"],
        "total_visits": 5
    }
]

def add_new_country(country, visits, cities):
    new_record = {"country":country, "cities_visited": cities, "total_visits": visits}
    travel_log.append(new_record)


add_new_country("Russia", 2, ["Moscow", "Saint Peters"])

