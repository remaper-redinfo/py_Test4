import folium
import pandas as pd
import urllib.request
import datetime
import time
import json
import webbrowser
import re

# [CODE 1]


def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("Authorization", "KakaoAK 174cbf5d17febfdc40dedd9f43f5d31f")
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [CODE 2]


def getGeoData(address):

    address = re.sub(r'\([^)]*\)', '', address)
    address = address.strip()

    base = "https://dapi.kakao.com/v2/local/search/keyword"

    try:
        parameters = "?query=%s" % urllib.parse.quote(address)
    except:
        return None

    url = base + parameters

    retData = get_request_url(url)
    if retData == None:
        return None

    jsonAddress = json.loads(retData)

    if 'documents' in jsonAddress.keys():
        if len(jsonAddress['documents']) != 0:
            latitude = jsonAddress['documents'][0]['y']
            longitude = jsonAddress['documents'][0]['x']
            print(jsonAddress['documents'][0]['address_name'] +
                  "::좌표: "+latitude + "," + longitude)
            return [latitude, longitude]
        else:
            return None


def main():

    # [CODE 3]
    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    filename = 'kakaomapRest/서울시 초등학교 현황.csv'
    df = pd.DataFrame.from_csv(
        filename, encoding='CP949', index_col=0, header=0)
    df = df.iloc[1:10, :]
    geoData = []

    # [CODE 4]
    for index, row in df.iterrows():
        geoData = getGeoData(row['주소'])
        if geoData != None:
            folium.Marker(geoData, popup=row['학교명'], icon=folium.Icon(
                color='red')).add_to(map)

    svFilename = 'elementary_school.html'
    map.save(svFilename)
    webbrowser.open(svFilename)


if __name__ == "__main__":
    main()
