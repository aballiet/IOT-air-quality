import requests
import time

IQAIR_API_KEY = '495bac73-2703-4612-8e45-14d54ccc5b90'
IQAIR_URL = "http://api.airvisual.com/v2/city?city=Villeurbanne&state=Auvergne-Rhône-Alpes&country=France&key=" + IQAIR_API_KEY 

TS_API_KEY = 'KDKR5U17UBHBSF5U'
TS_URL = 'https://api.thingspeak.com/update?api_key=' + TS_API_KEY

def update_api():
    while(True):
        iqair_response = requests.get(IQAIR_URL)
        iqair_content = iqair_response.json()
        pollution_measurements = iqair_content["data"]["current"]["pollution"]

        created_at = field1 = pollution_measurements["ts"]
        aqius = pollution_measurements["aqius"]
        mainus = pollution_measurements["mainus"]
        aqicn = pollution_measurements["aqicn"]
        maincn = pollution_measurements["maincn"]

        url = TS_URL + '&field1=' + str(aqius) + '&field2=' + str(mainus) + '&field3=' + str(aqicn) + '&field4=' + str(maincn) + '&created_at=' + str(created_at)
        thing_response = requests.get(url)

        time.sleep(3600)
    

if __name__ =='__main__':
    update_api()