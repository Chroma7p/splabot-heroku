import requests
import json
def get_spla_info(p1,p2):

    header={"user-agent":"splatoon3-notification-bot/0.1, Twitter @Chroma7p)"}
    res=requests.get(f"https://spla3.yuu26.com/api/{p1}/{p2}",headers=header)
    #print(res.status_code)
    if res.status_code == 200:
        #print(res.text)
        result=json.loads(res.text)
        if not "results" in result:
            return result["result"]
        return result["results"]
    return {"fail":True}