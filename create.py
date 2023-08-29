import requests

event_name = "Astrid"
api_key = "d1EB0p5CsBF_DZhbPAbsOS"

# create url
url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/d1EB0p5CsBF_DZhbPAbsOS"

# json_data = {"value": "james","value2": "hey"}
response = requests.post(url)

# deubg response
print(response.text)

if response.status_code == 200:
    print("request sent successfully")

else:
    print("request failed")