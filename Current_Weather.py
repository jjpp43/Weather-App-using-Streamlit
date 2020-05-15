import streamlit as st
import requests
import json

api_key = 'hidden'
api_url = f'http://api.airvisual.com/v2/states?country=USA&key={api_key}'


payload = {}
files = {}
headers = {}

response = requests.request("GET", api_url, headers=headers, data = payload, files = files).text.encode('utf8')
#Get the list of states
state_json = json.loads(response)

state_results = []

for i in state_json["data"]:
    state_results.append(i["state"])

state = st.selectbox("Please select a state", state_results)

#Get the list of cities in the selected state
city_list_url = f'http://api.airvisual.com/v2/cities?state={state}&country=USA&key={api_key}'
city_response = requests.request("GET", city_list_url, headers=headers, data = payload, files = files).text.encode('utf8')
#json
city_json = json.loads(city_response)

city_results = []

for city in city_json["data"]:
    city_results.append(city["city"])

city = st.selectbox("Please select a city", city_results)

#Get data of the selected city
city_info_url = f'http://api.airvisual.com/v2/city?city={city}&state={state}&country=USA&key={api_key}'
city_info_response = requests.request("GET", city_info_url, headers=headers, data = payload, files = files).text.encode('utf8')
#json 
city_info_json = json.loads(city_info_response)

city_coordinate = [city_info_json["data"]["location"]["coordinates"][0], city_info_json["data"]["location"]["coordinates"][1]]

st.header('Weather of the city')
st.subheader('longitude: ' + str(city_coordinate[0]))
st.subheader('latitude: ' + str(city_coordinate[1]))
st.subheader('Last update: ' + str(city_info_json["data"]["current"]["pollution"]["ts"]))
st.subheader('Air Quality Index(US): ' + str(city_info_json["data"]["current"]["pollution"]["aqius"]))
st.subheader('Temperature: ' + str(city_info_json["data"]["current"]["weather"]["tp"]) + ' °C')
st.subheader('Humidity: ' + str(city_info_json["data"]["current"]["weather"]["hu"]))
