#!bin/bash
deleteFile()
{
	FILE=$1
	if [[ -f "$FILE" ]]; then
    	rm "$FILE"
	fi
}
getGeoLocation()
{
	deleteFile location.txt
	latitude=$(curl -s https://json.geoiplookup.io/"$(curl -s https://ipinfo.io/ip)" | jq '.latitude')
	longitude=$(curl -s https://json.geoiplookup.io/"$(curl -s https://ipinfo.io/ip)" | jq '.longitude')
	echo "$latitude"
	echo "$longitude"
	deleteFile weatherData.json
	curl -s https://api.openweathermap.org/data/2.5/onecall?lat="$latitude"\&lon="$longitude"\&exclude=minutely,hourly\&appid=4a7d63f695a6c50153cba0e4d5b5c27e | jq  > weatherData.json
    chmod 600 weatherData.json
}

getGeoLocation 
python3 main.py
