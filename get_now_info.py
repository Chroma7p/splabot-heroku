from get_spla_info import get_spla_info
from datetime import datetime



def maketext():
    schedule=get_spla_info("schedule","")
    if "fail" in schedule :
        return "情報の取得に失敗しました"

    text="**現在のステージ&ルール**\n"
    start:datetime=datetime.strptime(schedule["regular"][0]["start_time"],"%Y-%m-%dT%H:%M:%S%z")
    end:datetime=datetime.strptime(schedule["regular"][0]["end_time"],"%Y-%m-%dT%H:%M:%S%z")
    text+=f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n\n"
    for typ in ["regular","bankara_challenge","bankara_open","x"]:
        if typ=="regular":
            text+="**レギュラーマッチ**\n"
        elif typ=="bankara_challenge":
            text+="**バンカラチャレンジ**\n"
        elif typ=="bankara_open":
            text+="**バンカラオープン**\n"
        elif typ=="x":
            text+="**Xマッチ**\n"
        now_info=schedule[typ][0]
        if typ!="regular":
            rule=now_info["rule"]["name"]
            next_info=schedule[typ][1]
            next_rule=next_info["rule"]["name"]
            text+=f"***{rule}*** -> ({next_rule})\n"
        stages=now_info["stages"]
        text+=f"{stages[0]['name']}・{stages[1]['name']}\n\n"

    return text