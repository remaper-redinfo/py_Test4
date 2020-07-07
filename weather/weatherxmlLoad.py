from bs4 import BeautifulSoup

xstring = open("myxmlfile.xml", "r")
soup = BeautifulSoup(xstring, 'xml')
# print(soup.text)
items = soup.find_all('item')
# print(items)
datalist = []

for item in items:
    weatherData = {
        "date": '',
        "location": '',
        "avgTemp": '',
        "minTemp": '',
        "maxTemp": ''
    }
    weatherData["date"] = item.find("tm").text
    weatherData["location"] = item.find("stnId").text
    weatherData["avgTemp"] = item.find("avgTa").text
    weatherData["minTemp"] = item.find("minTa").text
    weatherData["maxTemp"] = item.find("maxTa").text
    datalist.append(weatherData)

print(datalist)

# xstring = re.sub(r"\s+", "", xstring)

# dom = minidom.parseString(xstring)

# items = dom.getElementsByTagName("item")
