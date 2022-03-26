#!/bin/bash
deleteFile()
{
	FILE=$1
	if [[ -f "$FILE" ]]; then
    	rm "$FILE"
	fi
}
getWeatherData()
{
	#初步想改成这样
	curl http://ip-api.com/json/ | jq . > ip.json
	#接着用awk抓latitude和longitude
	

	latitude=$(curl -s https://json.geoiplookup.io/"$(curl -s https://ipinfo.io/ip)" | jq '.latitude')
	longitude=$(curl -s https://json.geoiplookup.io/"$(curl -s https://ipinfo.io/ip)" | jq '.longitude')
	unit=imperial
	deleteFile weatherData.json
	curl -s https://api.openweathermap.org/data/2.5/onecall?lat="$latitude"\&lon="$longitude"\&units="$unit"\&exclude=minutely,hourly\&appid=4a7d63f695a6c50153cba0e4d5b5c27e | jq  > weatherData.json
    chmod 600 weatherData.json
}

getWeatherData 
bash createTable.sh
python3 main.py
#DROP TABLE visit_infomation, weather_current, weather_daily;


