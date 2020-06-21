import pandas as pd
import requests
import json

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
area = requests.get(url).json()
data = json.loads(area['data'])
update_time = data['lastUpdateTime']
all_counties = data['areaTree']
all_list = []
for country_data in all_counties:
    if country_data['name'] != '中国':
        continue
    else:
        all_provinces = country_data['children']
        for province_data in all_provinces:
            province_name = province_data['name']
            all_cities = province_data['children']
            for city_data in all_cities:
                city_name = city_data['name']
                city_total = city_data['total']
                province_result = {'省份': province_name, '城市': city_name, '更新时间': update_time}
                province_result.update(city_total)
                all_list.append(province_result)
df = pd.DataFrame(all_list)
df.to_csv('data.csv', index=False, encoding="utf_8_sig")

import pandas as pd
import requests
import json

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
area = requests.get(url).json()
data = json.loads(area['data'])
update_time = data['lastUpdateTime']
all_counties = data['areaTree']
all_list = []
for country_data in all_counties:
    if country_data['name'] != '中国':
        continue
    else:
        all_provinces = country_data['children']
        for province_data in all_provinces:
            province_name = province_data['name']
            all_cities = province_data['children']
            for city_data in all_cities:
                city_name = city_data['name'] 
                city_total = city_data['total']
                province_result = {'省份': province_name, '城市': city_name, '更新时间': update_time}
                province_result.update(city_total)
                all_list.append(province_result)#将当前省份的数据添加到数据列表里面

df = pd.DataFrame(all_list)
df.to_csv('data.csv', index=False, encoding="utf_8_sig")

