# -*- coding: utf-8 -*-

import pandas as pd
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium.features import DivIcon
from tqdm import tqdm


def replace_escape(s):
    rt = str(s).replace('`', '\`')
    return rt


df_school_all = pd.read_csv('./back_data/2021.12.31/학교기본정보_위치정보포함.csv', encoding='CP949')

seoul_cityhall = [37.5666805, 126.9784147]
gwangju_cityhall = [35.16015532628239, 126.85146388158552]

# m = folium.Map(location=seoul_cityhall, tiles='openstreetmap', zoom_start=13)
m = folium.Map(location=gwangju_cityhall, tiles='openstreetmap', zoom_start=13)

group_all_school = folium.FeatureGroup(name='초중고 전체', overlay=True, show=True)
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

df_school_all = df_school_all.dropna(subset=['Latitude'])
df_school_all = df_school_all.dropna(subset=['Longitude'])

# 초등학교 DataFrame
mask_elementary_school = df_school_all['학교종류명'] == '초등학교'
df_elementary_school = df_school_all[mask_elementary_school]
# print(df_elementary_school)

# 중학교 DataFrame
mask_middle_school = df_school_all['학교종류명'] == '중학교'
df_middle_school = df_school_all[mask_middle_school]
# print(df_middle_school)

# 고등학교 DataFrame
mask_high_school = df_school_all['학교종류명'] == '고등학교'
df_high_school = df_school_all[mask_high_school]
# print(df_high_school)


# 초중고 MarkerCluster
mc_all_school = MarkerCluster()

# 초등학교 MarkerCluster
mc_elementary_school = MarkerCluster()
for _, row in tqdm(df_elementary_school.iterrows()):
    mc_elementary_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='blue'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

    mc_all_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='blue'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

group_elementary_school.add_child(mc_elementary_school)
group_all_school.add_child(mc_all_school)

# 중학교 MarkerCluster
mc_middle_school = MarkerCluster()
for _, row in tqdm(df_middle_school.iterrows()):
    mc_middle_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='green'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

    mc_all_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='green'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

group_middle_school.add_child(mc_middle_school)
group_all_school.add_child(mc_all_school)

# 고등학교 MarkerCluster
mc_high_school = MarkerCluster()
for _, row in tqdm(df_high_school.iterrows()):
    mc_high_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='orange'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

    mc_all_school.add_child(
        Marker(location=[row['Latitude'], row['Longitude']],
               icon=folium.Icon(icon='home', color='orange'),
               popup=folium.Popup(
                   f"<div style = font-size:1.5em; margin-bottom: 1px;> <strong>[{row['학교명']}]</strong> </div>" \
                   f"{replace_escape(row['영문학교명'])} <br>표준학교코드: {row['표준학교코드']}" \
                   f"<br>도로명주소: {replace_escape(row['도로명주소']) + replace_escape(row['도로명상세주소'])}" \
                   f"<br>관할조직명: {row['관할조직명']}" \
                   f"<br>학교구분: {row['고등학교일반실업구분명']}, {row['설립명']}, {row['남녀공학구분명']}, {row['입시전후기구분명']}" \
                   f"<br>전화번호: {row['전화번호']} <br>팩스번호: {row['팩스번호']}" \
                   f"<br>홈페이지주소: {row['홈페이지주소']} <br>설립일자/개교기념일: {row['설립일자']}/{row['개교기념일']}<br>정보수정일: {row['수정일']}",
                   max_width=300), )
    )

group_high_school.add_child(mc_high_school)
group_all_school.add_child(mc_all_school)

title1 = '<a href="/" target="_blank">[우킹우 맵툴] </a> 2022 전국 초중고교 지도'
title_html1 = '''
             <h3 align="center" ><b>{}</b></h3>
             '''.format(title1)

title_html = title_html1

m.get_root().html.add_child(folium.Element(title_html))

m.save('index.html')
