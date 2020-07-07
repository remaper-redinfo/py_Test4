# 2020-07-07 수업
# 기상자료개방포털의 open API(공공데이터 연계)를 이용하여 데이터를 가져오고 저장하고
# 출력해보자.
# 기상자료개방포털 https://data.kma.go.kr/
# 기상자료 open API https://data.kma.go.kr/api/selectApiList.do?pgmNo=42
# 공공데이터포털 https://www.data.go.kr/

# 공공데이터포털에서 serviceKey를 받고 시작해야 한다. (쉬움)
# 90일 이전 데이터만 취합 가능(실시간은 안됨)

import urllib.request
import json
from xml.dom import minidom

# 서비스키와 검색시작날짜 검색종료날짜 변수화하여 변경에 용잉하게 만들기
serviceKey = "u1787ibmOGLYJ8lrbxwPk3MauGKscWK%2BYHPhsXnslQqFvGaN67hTnAfYc288yxkVGUdJzw92MvOJ%2BkGuORJBxw%3D%3D"
startDt = "20190101"
endDt = "20191231"
stnIds = "108"  # 지역을 의미(108은 서울)

# url setting (기상청02_지상_종관__ASOS__일자료_조회서비스_오픈API활용가이드.docx)
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey="+serviceKey + \
    "&numOfRows=365&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=" + \
    startDt+"&endDt="+endDt+"&stnIds="+stnIds

# urllib으로 http 통신 => HTTPResponse
response = urllib.request.urlopen(url)

# print(response.read())

# if response.status == 200:
#     print(response.read())
# else:
#     print("HTTP not Response")

# minidom을 이용하여 XML 파싱 <-- 코드 전개가 쉽다.
# import xml.etree.ElementTree 이것도 많이 사용하고 있다. <-- XML 구성이 쉽다
dom = minidom.parse(response)

# 파일 만들기
f = open("myxmlfile.xml", "w")
dom.writexml(f, indent='\t', addindent='\t',  newl='\n')
f.close()
# 파일만들기 끝

# minidom으로 만든 Document Object로 컨트롤
# 저장된 파일을 살펴보면서 어떤 Element를 가져올지 탐색해 보자
items = dom.getElementsByTagName("item")

# items에 저장된 Object를 이해해 보고 특정 변수를 가져와 보자
print(type(items))
print(items.length)

print(type(items[0].childNodes[1]))
print(items[0].childNodes[1])
print(items[0].childNodes[1].nodeName)

print(type(items[0].childNodes[1].childNodes[0]))
print(items[0].childNodes[1].childNodes[0])

print(items[0].childNodes[1].firstChild.nodeValue)
print(items[0].childNodes[1].lastChild.nodeValue)
print(items[0].childNodes[1].childNodes[0].nodeValue)

# xml 타입을 dic 타입으로 변경하고 리스트에 저장
datalist = []

for item in items:
    weatherData = {
        "date": '',
        "location": '',
        "avgTemp": '',
        "minTemp": '',
        "maxTemp": ''
    }
    node = item.childNodes
    weatherData["date"] = node[1].childNodes[0].nodeValue
    weatherData["location"] = node[0].childNodes[0].nodeValue
    weatherData["avgTemp"] = node[2].childNodes[0].nodeValue
    weatherData["minTemp"] = node[3].childNodes[0].nodeValue
    weatherData["maxTemp"] = node[5].childNodes[0].nodeValue

    datalist.append(weatherData)

print(datalist)

# 리스트에 저장된 weather data를 Json으로 변경

# json_val = json.dumps(datalist)

json_test_dict = json.dumps(
    datalist, ensure_ascii=False, indent=4).encode('utf-8')

f = open("myjsonfile.json", "wb")
f.write(json_test_dict)
f.close()
