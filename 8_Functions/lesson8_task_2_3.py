def make_country(country, capital, **countries):
    country_dict = {}
    country_dict[country] = capital
    for i, j in countries.items():
        country_dict[i] = j
    return country_dict.values()

print(make_country('Ukraine', 'Kyiv', Poland='Warsaw', Germany='Berlin'))
