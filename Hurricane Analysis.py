# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
new_damages = []
for items in damages:
    if items[-1] == "M":
        items = items.strip("M")
        items = float(items) * 1000000
        new_damages.append(int(items))
    elif items[-1] == "B":
        items = items.strip("B")
        items = float(items) * 1000000000
        new_damages.append(int(items))
    else:
        new_damages.append(0)

# 2
# Create a Table
# print(new_damages)
# Create and view the hurricanes dictionary
hurricane_dictionary = [
    {"Name": n, "Month": m, "Year": y, "Max Sustained Wind": w, "Areas Affected": a, "Damage": nd, "Deaths": d} for
    n, m, y, w, a, nd, d in zip(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)]


# print(hurricane_dictionary)
# 3
# Organizing by Year

def year_finder(year):
    current_year = []
    for dictionary in hurricane_dictionary:
        if (dictionary["Year"] == year):
            current_year.append(dictionary)
    return current_year


# print(year_finder(1932))
# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas
def area_affected_count(area):
    area_count = []
    for dictionary in hurricane_dictionary:
        for areas in dictionary["Areas Affected"]:
            if areas == area:
                area_count.append(area)
                area_count = [1 for items in area_count]
                area_sum = sum(area_count)

    return f"{area}: {area_sum}"


print(area_affected_count("Yucatn Peninsula"))

# create dictionary of areas to store the number of hurricanes involved in


# 5
# Calculating Maximum Hurricane Count
max_affected = max(hurricane_dictionary, key=lambda x: x['Areas Affected'])
# print(max_affected)
# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
max_deaths = max(hurricane_dictionary, key=lambda x: x["Deaths"])
# print(max_deaths)
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
new_dict = []
for dictionary in hurricane_dictionary:
    dictionary["Mortality Rate"] = ""
    if dictionary["Deaths"] > 10000:
        dictionary["Mortality Rate"] = 4
        new_dict.append(dictionary)
    elif dictionary["Deaths"] >= 1000:
        dictionary["Mortality Rate"] = 3
        new_dict.append(dictionary)
    elif dictionary["Deaths"] >= 500:
        dictionary["Mortality Rate"] = 2
        new_dict.append(dictionary)
    elif dictionary["Deaths"] >= 100:
        dictionary["Mortality Rate"] = 1
        new_dict.append(dictionary)
    else:
        dictionary["Mortality Rate"] = 0
        new_dict.append(dictionary)


# 8 Calculating Hurricane Maximum Damage
max_damage = max(hurricane_dictionary, key=lambda x:x["Damage"])
# find highest damage inducing hurricane and its total cost
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


for dictionary in hurricane_dictionary:
  dictionary["Damage Scale"] = ""
  if dictionary["Damage"] > 50000000000:
    dictionary["Damage Scale"] = 4
    new_dict.append(dictionary)
  elif dictionary["Damage"] >= 10000000000:
    dictionary["Damage Scale"] = 3
    new_dict.append(dictionary)
  elif dictionary["Damage"] >= 1000000000:
    dictionary["Damage Scale"] = 2
    new_dict.append(dictionary)
  elif dictionary["Damage"] >= 100000000:
    dictionary["Damage Scale"] = 1
    new_dict.append(dictionary)
  else:
    dictionary["Damage Scale"] = 0
    new_dict.append(dictionary)
print(new_dict)



