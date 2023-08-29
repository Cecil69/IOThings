import requests

class IFTTT_notification:
    def __init__(self, event_name = "Astrid", api_key = "d1EB0p5CsBF_DZhbPAbsOS") :
        self.event_name = event_name
        self.api_key = api_key

    def Send_mail (self):
        # create url
        url = f"https://maker.ifttt.com/trigger/{self.event_name}/json/with/key/{self.api_key}"

        # json_data = {"value": "james","value2": "hey"}
        response = requests.post(url)

        # deubg response
        print(response.text)

        if response.status_code == 200:
            print("request sent successfully")

        else:
            print("request failed")