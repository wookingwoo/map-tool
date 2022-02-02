import pandas as pd
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium.features import DivIcon
from tqdm import tqdm

df_school_all = pd.read_csv('./back_data/2021-09-15/전국초중등학교위치표준데이터.csv', encoding='CP949')

seoul_cityhall = [37.5666805, 126.9784147]
gwangju_cityhall = [35.16015532628239, 126.85146388158552]

m = folium.Map(location=seoul_cityhall, tiles='openstreetmap', zoom_start=13)
# m = folium.Map(location=gwangju_cityhall, tiles='openstreetmap', zoom_start=13)

group_all_school = folium.FeatureGroup(name='초중고', overlay=True, show=True)
group_elementary_school = folium.FeatureGroup(name='초등학교', overlay=True, show=False)
group_middle_school = folium.FeatureGroup(name='중학교', overlay=True, show=False)
group_high_school = folium.FeatureGroup(name='고등학교', overlay=True, show=False)
group_seoul_cityhall = folium.FeatureGroup(name='서울시청 위치', overlay=True)

group_all_school.add_to(m)
group_elementary_school.add_to(m)
group_middle_school.add_to(m)
group_high_school.add_to(m)

folium.LayerControl().add_to(m)

Marker(location=seoul_cityhall,
       popup=folium.Popup("서울시청", max_width=300),
       icon=folium.Icon(color='red', icon='star')
       ).add_to(m)

df_school_all = df_school_all.dropna(subset=['위도'])
df_school_all = df_school_all.dropna(subset=['경도'])

# 초등학교 DataFrame
mask_elementary_school = df_school_all['학교급구분'] == '초등학교'
df_elementary_school = df_school_all[mask_elementary_school]
# print(df_elementary_school)

# 중학교 DataFrame
mask_middle_school = df_school_all['학교급구분'] == '중학교'
df_middle_school = df_school_all[mask_middle_school]
# print(df_middle_school)

# 고등학교 DataFrame
mask_high_school = df_school_all['학교급구분'] == '고등학교'
df_high_school = df_school_all[mask_high_school]
# print(df_high_school)


# 초중고 MarkerCluster
mc_all_school = MarkerCluster()

# 초등학교 MarkerCluster
mc_elementary_school = MarkerCluster()
for _, row in tqdm(df_elementary_school.iterrows()):
    mc_elementary_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='blue'),
               popup=folium.Popup("[초등학교]<br>" + row['학교명'], max_width=300)
               )
    )

    mc_all_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='blue'),
               popup=folium.Popup("[초등학교]<br>" + row['학교명'], max_width=300)
               )
    )

group_elementary_school.add_child(mc_elementary_school)
group_all_school.add_child(mc_all_school)

# 중학교 MarkerCluster
mc_middle_school = MarkerCluster()
for _, row in tqdm(df_middle_school.iterrows()):
    mc_middle_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='green'),
               popup=folium.Popup("[중학교]<br>" + row['학교명'], max_width=300)
               )
    )

    mc_all_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='green'),
               popup=folium.Popup("[중학교]<br>" + row['학교명'], max_width=300)
               )
    )

group_middle_school.add_child(mc_middle_school)
group_all_school.add_child(mc_all_school)

# 고등학교 MarkerCluster
mc_high_school = MarkerCluster()
for _, row in tqdm(df_high_school.iterrows()):
    mc_high_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='orange'),
               popup=folium.Popup("[고등학교]<br>" + row['학교명'], max_width=300)
               )
    )

    mc_all_school.add_child(
        Marker(location=[row['위도'], row['경도']],
               icon=folium.Icon(icon='home', color='orange'),
               popup=folium.Popup("[고등학교]<br>" + row['학교명'], max_width=300)
               )
    )

group_high_school.add_child(mc_high_school)
group_all_school.add_child(mc_all_school)

title1 = '전국 초중고교 위치'
title_html1 = '''
             <h3 align="center" ><b>{}</b></h3>
             '''.format(title1)

title_html = title_html1

m.get_root().html.add_child(folium.Element(title_html))

m.save('index.html')
m
