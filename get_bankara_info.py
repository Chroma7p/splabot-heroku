from get_spla_info import get_spla_info
from datetime import datetime



def maketext(is_open=True):
    if is_open:
        schedule=get_spla_info("bankara-open","schedule")
    else:
        schedule=get_spla_info("bankara-challenge","schedule")
    if "fail" in schedule:
        return "情報の取得に失敗しました"
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
        if day["is_fest"]:
            text+="フェス期間だからないよ！\n"
        else:
            rule=day["rule"]
            text+=f"**{rule['name']}**\n"
            stages=day["stages"]
            for stage in stages:
                text+=f"{stage['name']}\n"
        text+="\n"

        

    return text

