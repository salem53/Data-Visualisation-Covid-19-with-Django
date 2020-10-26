from operator import itemgetter
from django.contrib.auth import get_user_model
user = get_user_model()
from covid import Covid
import pandas as pd
df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
dic=df.to_dict('split')
column=dic['columns']
data1=dic['data']
index=dic['index']
world_dates_day_by_day=[]
world_cases_day_by_day=[]
world_deaths_day_by_day=[]

#collect_data_day_per_day
for day in data1 :
    for info in day :
        if info == "World" and day.index(info) == 2:
            world_cases_day_by_day.append(day[5]), world_dates_day_by_day.append(
                day[3]), world_deaths_day_by_day.append((day[8]))
#countries_lists
europe_countries=["Russia","Spain","UK","Italy","Germany","France","Sweden","Belarus","Ukraine", "Belgium","Netherlands","Portugal","Romania","Poland","Switzerland","Ireland","Serbia","Moldova","Austria","Czechia","Denmark","Bosnia and Herzegovina","Bulgaria","North Macedonia","Norway","Finland","Luxembourg","Albania","Croatia","Hungary","Greece","Montenegro","Slovakia","Slovenia","Estonia","Lithuania","Iceland","Latvia","Andorra","Malta","San Marino","Channel Islands","Isle of Man","Faeroe Islands","Gibraltar","Monaco","Liechtenstein","Vatican City"]
north_america_countries=["USA","Mexico","Canada","Dominican Republic","Panama","Guatemala","Honduras","Costa Rica","El Salvador","Haiti","Nicaragua","Cuba","Jamaica","Bahamas","Martinique","Guadeloupe","Cayman Islands","Bermuda","Trinidad and Tobago","Aruba","Sint Maarten","Barbados","Turks and Caicos","Antigua and Barbuda","St. Vincent Grenadines","Saint Martin","Belize","Curaçao","Saint Lucia","Grenada","Dominica","Saint Kitts and Nevis","Greenland","Montserrat","Caribbean Netherlands","British Virgin Islands","St. Barth","Saint Pierre Miquelon","Anguilla"]
asia_countries= ["India","Iran","Pakistan","Saudi Arabia","Bangladesh","Turkey","Iraq","Qatar","Indonesia","Kazakhstan","China","Philippines","Oman","Israel","Kuwait","UAE","Singapore","Bahrain","Armenia","Afghanistan","Kyrgyzstan","Azerbaijan","Japan","Uzbekistan","Nepal", "S. Korea","Palestine","Malaysia","Tajikistan","Lebanon","Maldives","Thailand","Hong Kong","Sri Lanka","Yemen","Jordan","Georgia","Cyprus","Syria","Taiwan","Vietnam","Myanmar","Mongolia","Cambodia","Brunei","Bhutan","Macao","Timor-Leste","Laos"]
south_america_countries=["Brazil","Peru","Chile","Colombia","Argentina","Ecuador","Bolivia","Venezuela","French Guiana","Paraguay","Suriname","Uruguay","Guyana", "Falkland Islands"]
oceania_countries=["Australia","New Zealand","Papua New Guinea","French Polynesia","Fiji","New Caledonia"]
africa_countries=['South Africa', 'Egypt', 'Nigeria', 'Ghana', 'Algeria', 'Morocco', 'Kenya', 'Cameroon', 'Ivory Coast', 'Ethiopia', 'Sudan', 'Madagascar', 'Senegal', 'DRC', 'Gabon', 'Guinea', 'Mauritania', 'Djibouti', 'Zambia', 'CAR', 'Malawi', 'Congo', 'Somalia', 'Equatorial Guinea', 'Mayotte', 'Libya', 'Zimbabwe', 'Mali', 'Cabo Verde', 'Eswatini', 'South Sudan', 'Guinea-Bissau', 'Namibia', 'Rwanda', 'Sierra Leone', 'Benin', 'Mozambique', 'Tunisia', 'Liberia', 'Uganda', 'Niger', 'Burkina Faso', 'Angola', 'Chad', 'Togo', 'Sao Tome and Principe', 'Botswana','Réunion', 'Tanzania', 'Lesotho', 'Burundi', 'Comoros', 'Mauritius', 'Gambia', 'Eritrea', 'Seychelles', 'Western Sahara']
all_countries=europe_countries+north_america_countries+asia_countries+south_america_countries+oceania_countries+africa_countries

europe = []
asia = []
africa = []
oceania = []
south_america = []
north_america = []
continents_names=[]
continents_total_cases=[]
continents_active_cases=[]
def transform_data_to_list():
    L=[]
    data=Covid(source="worldometers")
    # getting data by country


    for cnt in asia_countries:
        asia.append(data.get_status_by_country_name(cnt))

    for cnt in africa_countries:
        africa.append(data.get_status_by_country_name(cnt))

    for cnt in oceania_countries:
        oceania.append(data.get_status_by_country_name(cnt))

    for cnt in south_america_countries:
        south_america.append(data.get_status_by_country_name(cnt))

    for cnt in north_america_countries:
        north_america.append(data.get_status_by_country_name(cnt))

    for cnt in europe_countries:
        europe.append(data.get_status_by_country_name(cnt))
    countries=data.list_countries()
    for c in countries:
        L.append(data.get_status_by_country_name(c))
    return L

#tranforming data to list
covid1=transform_data_to_list()
#data_of_continetns
continents=covid1[:5]
continents=sorted(continents, key=itemgetter('confirmed'),reverse=True)
for cnt in continents:
    cnt.pop("total_tests_per_million", None)
    for k, v in cnt.items():

        if k == "country":
            continents_names.append(v)
        if k == "confirmed":
            continents_total_cases.append(v)
        if k == "active":
            continents_active_cases.append(v)


#data_all_countries_one_by_one
covid1=covid1[8:]
#sorting data
covid1=sorted(covid1, key=itemgetter('confirmed'),reverse=True)
europe=sorted(europe, key=itemgetter('confirmed'),reverse=True)
#filtring coutnries per continent
europe_countries=["Europe","Russia","Spain","UK","Italy","Germany","France","Sweden","Belarus","Ukraine", "Belgium","Netherlands","Portugal","Romania","Poland","Switzerland","Ireland","Serbia","Moldova","Austria","Czechia","Denmark","Bosnia and Herzegovina","Bulgaria","North Macedonia","Norway","Finland","Luxembourg","Albania","Croatia","Hungary","Greece","Montenegro","Slovakia","Slovenia","Estonia","Lithuania","Iceland","Latvia","Andorra","Malta","San Marino","Channel Islands","Isle of Man","Faeroe Islands","Gibraltar","Monaco","Liechtenstein","Vatican City"]
north_america_countries=["USA","Mexico","Canada","Dominican Republic","Panama","Guatemala","Honduras","Costa Rica","El Salvador","Haiti","Nicaragua","Cuba","Jamaica","Bahamas","Martinique","Guadeloupe","Cayman Islands","Bermuda","Trinidad and Tobago","Aruba","Sint Maarten","Barbados","Turks and Caicos","Antigua and Barbuda","St. Vincent Grenadines","Saint Martin","Belize","Curaçao","Saint Lucia","Grenada","Dominica","Saint Kitts and Nevis","Greenland","Montserrat","Caribbean Netherlands","British Virgin Islands","St. Barth","Saint Pierre Miquelon","Anguilla"]
asia_countries= ["India","Iran","Pakistan","Saudi Arabia","Bangladesh","Turkey","Iraq","Qatar","Indonesia","Kazakhstan","China","Philippines","Oman","Israel","Kuwait","UAE","Singapore","Bahrain","Armenia","Afghanistan","Kyrgyzstan","Azerbaijan","Japan","Uzbekistan","Nepal", "S. Korea","Palestine","Malaysia","Tajikistan","Lebanon","Maldives","Thailand","Hong Kong","Sri Lanka","Yemen","Jordan","Georgia","Cyprus","Syria","Taiwan","Vietnam","Myanmar","Mongolia","Cambodia","Brunei","Bhutan","Macao","Timor-Leste","Laos"]
south_america_countries=["Brazil","Peru","Chile","Colombia","Argentina","Ecuador","Bolivia","Venezuela","French Guiana","Paraguay","Suriname","Uruguay","Guyana", "Falkland Islands"]
oceania_countries=["Australia","New Zealand","Papua New Guinea","French Polynesia","Fiji","New Caledonia"]
africa_countries=['South Africa', 'Egypt', 'Nigeria', 'Ghana', 'Algeria', 'Morocco', 'Kenya', 'Cameroon', 'Ivory Coast', 'Ethiopia', 'Sudan', 'Madagascar', 'Senegal', 'DRC', 'Gabon', 'Guinea', 'Mauritania', 'Djibouti', 'Zambia', 'CAR', 'Malawi', 'Congo', 'Somalia', 'Equatorial Guinea', 'Mayotte', 'Libya', 'Zimbabwe', 'Mali', 'Cabo Verde', 'Eswatini', 'South Sudan', 'Guinea-Bissau', 'Namibia', 'Rwanda', 'Sierra Leone', 'Benin', 'Mozambique', 'Tunisia', 'Liberia', 'Uganda', 'Niger', 'Burkina Faso', 'Angola', 'Chad', 'Togo', 'Sao Tome and Principe', 'Botswana','Réunion', 'Tanzania', 'Lesotho', 'Burundi', 'Comoros', 'Mauritius', 'Gambia', 'Eritrea', 'Seychelles', 'Western Sahara']



#formating digits with ","
#all_world
for cnt in covid1 :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():

        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#europe
for cnt in europe :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#asia
for cnt in asia :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#oceania
for cnt in oceania :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#africa
for cnt in africa :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#north_america
for cnt in north_america :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#formating digits with ","
#south_america
for cnt in south_america :
    cnt.pop("total_tests_per_million", None)
    for k,v in cnt.items():
        if k!="country" :
            cnt[k]=format(v,",")
            if v==0 :
                cnt[k] = ""
            elif (k=="new_cases" or k=="new_deaths") :
                cnt[k] ="+"+cnt[k]
#get world and other continents data
#world
covid=Covid(source="worldometers")

from django.contrib.auth import get_user_model
user = get_user_model()
world =covid.get_status_by_country_name("World")
world.pop("total_tests_per_million",None)
for k, v in world.items():
    if k != "country":
        world[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]
#get world and other continents data
#europe
europe_all =covid.get_status_by_country_name("Europe")
europe_all.pop("total_tests_per_million",None)
for k, v in europe_all.items():
    if k != "country":
        europe_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]

#get world and other continents data
#asia
asia_all =covid.get_status_by_country_name("Asia")
asia_all.pop("total_tests_per_million",None)
for k, v in asia_all.items():
    if k != "country":
        asia_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]

#get world and other continents data
#africa
africa_all =covid.get_status_by_country_name("Africa")
africa_all.pop("total_tests_per_million",None)
for k, v in africa_all.items():
    if k != "country":
        africa_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]

#get world and other continents data
#oceania
oceania_all =covid.get_status_by_country_name("Oceania")
oceania_all.pop("total_tests_per_million",None)
for k, v in oceania_all.items():
    if k != "country":
        oceania_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]

#get world and other continents data
#north_america
north_america_all =covid.get_status_by_country_name("North America")
north_america_all.pop("total_tests_per_million",None)
for k, v in north_america_all.items():
    if k != "country":
        north_america_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]
#get world and other continents data
#south_america
south_america_all =covid.get_status_by_country_name("South America")
south_america_all.pop("total_tests_per_million",None)
for k, v in south_america_all.items():
    if k != "country":
        south_america_all[k]=format(v, ",")
        if v == 0:
            cnt[k] = ""
        elif (k == "new_cases" or k == "new_deaths"):
            cnt[k] = "+" + cnt[k]


def total_cases():
    return format(covid.get_total_confirmed_cases(),",")
def total_deaths():
    return format(covid.get_total_deaths(), ",")
def total_recovered():
    return format(covid.get_total_recovered(),",")
def active_cases():
    return format(covid.get_total_active_cases(), ",")
