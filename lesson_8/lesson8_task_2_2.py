def make_country(country_dict, country, capital):
    country_dict[country] = capital
    return country_dict
    

country_dict = {}
while True:
    country = input('Please, enter the COUNTRY (or press "q" to quit): ')
    if country == 'q':
        break
    capital = input('Now enter its CAPITAL (or press "q" to quit): ')
    if capital == 'q':
        break
    make_country(country_dict, country, capital)
for i, j in country_dict.items():
    print(j)
