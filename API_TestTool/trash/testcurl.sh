#/bin/bash
echo "root"
# curl -X GET -L 'http://127.0.0.1:8000/'
# curl -X GET -L 'http://127.0.0.1:8000/sample/'

ORG_URL='https://api.open-meteo.com/v1/forecast?latitude=35.6785&longitude=139.6823&current_weather=true'
# curl -X GET -L "$URL" 

forecastProxyURL='http://127.0.0.1:8000/v1/forecast?latitude=35.6785&longitude=139.6823&current_weather=true'
# curl -X GET -L "$forecastProxyURL"

# https://open-meteo.com/en/docs/historical-weather-api
archiveProxyURL='http://127.0.0.1:8000/v1/archive?latitude=35.6785&longitude=139.6823&current_weather=true'
curl -X GET -L "$archiveProxyURL"

# TESTURL='http://127.0.0.1:8000/v1/archive'
# curl -X GET -L "$TESTURL"
