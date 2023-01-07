from get_spla_info import get_spla_info
from datetime import datetime

def maketext():
    schedule=get_spla_info("coop-grouping","schedule")
    if "fail" in schedule:
        return "情報の取得に失敗しました",None
    text=""
    for i,day in enumerate(schedule[:3]):
        if i==0:
            text+="**現在**\n"
        elif i==1:
            text+="**つぎ**\n"
        elif i==2:
            text+="**そのつぎ**\n"
        start:datetime=datetime.strptime(day["start_time"],"%Y-%m-%dT%H:%M:%S%z")
        end:datetime=datetime.strptime(day["end_time"],"%Y-%m-%dT%H:%M:%S%z")
        text+=f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
        stage=day["stage"]["name"]
        text+=f"{stage}\n"
        weapons=day["weapons"]
        for weapon in weapons:
            text+=f"{weapon['name']}\n"
        text+="\n"
    return text,datetime.strptime(schedule[1]["start_time"],"%Y-%m-%dT%H:%M:%S%z")