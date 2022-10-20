def make_country(country, capital):
    country_dict = {}
    country_dict[country] = capital
    return country_dict.values()
    
print(make_country(input('Please, enter the country: '), 
                input('Now enter its capital: ')))
