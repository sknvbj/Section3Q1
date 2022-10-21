import requests
from dotenv import load_dotenv
load_dotenv()
import os

url =  "https://osome-public.p.rapidapi.com/time-series"

queries = {"start":"2021-05-01T00:00:00","q":"#KTBFFH","end":"2021-05-31T23:59:59"}

headers = {
	"X-RapidAPI-Key": os.environ['API_KEY'],
	"X-RapidAPI-Host": "osome-public.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=queries)

print(response.json()['result_url'])

data_url = response.json()['result_url']

response_2 = requests.get(data_url)

response_spaces = response_2.text
response_commas = response_spaces.replace('\t',',')
header = "Date,Number of Tweets that Contain Queried Hashtag"
print(response_commas)

file = open('api_data.csv', 'w')
file.write(header)
file.close()
file = open('api_data.csv', 'a')
file.write('\n')
file.write(response_commas)
file.close()








