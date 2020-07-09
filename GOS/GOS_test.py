import pandas as pd
import folium
import webbrowser
import chardet
import json

state_path = 'CTPRVN_wgs84.json'
state_geo = json.load(open(state_path, encoding='utf-8'))

state_unemployment = 'Total_People_2020_6.csv'

state_data = pd.read_csv(state_unemployment, encoding='EUC-KR')
state_data = state_data.astype({'Code': 'str', 'Population': 'float'})
print(state_data.dtypes)

# for row in state_data :


m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
# folium.Map(location=[37.566345, 126.977893], zoom_start=17, tiles='Stamen Terrain')
# folium.Map(location=[37.566345, 126.977893], zoom_start=17, tiles='Stamen Toner')

# folium.Marker([37.566345, 126.977893], popup='서울특별시청').add_to(map_osm)
# folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map_osm)

# folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
# folium.CircleMarker([37.5658859, 126.9754788], radius=100,color='#3186cc',fill_color='#3186cc', popup='덕수궁').add_to(map_osm)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['Code', 'Population'],
    key_on='feature.properties.CTPRVN_CD',
    fill_color='PuRd',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")
